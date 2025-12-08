"""
FastAPI application for emotion detection from audio.
"""

import os
import tempfile
import pickle
from pathlib import Path
from typing import Dict, Union

# Disable TensorFlow warnings before importing
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow.keras.models import load_model, model_from_json
from tensorflow.keras.utils import get_custom_objects


import librosa
import numpy as np
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Emotion Detection from Audio", version="1.0.0")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Model configuration
MODEL_DIR = os.path.join(os.path.dirname(__file__), "model")

# Check for different possible file naming patterns
MODEL_JSON_PATHS = [
    os.path.join(MODEL_DIR, "CNN_model.json"),
    os.path.join(MODEL_DIR, "Emotion_Voice_Detection_Model.json")
]
MODEL_WEIGHTS_PATHS = [
    os.path.join(MODEL_DIR, "CNN_model.weights.h5"),
    os.path.join(MODEL_DIR, "Emotion_Voice_Detection_Model.weights.h5")
]
MODEL_H5_PATH = os.path.join(MODEL_DIR, "Emotion_Voice_Detection_Model.h5")
SCALER_PATH = os.path.join(MODEL_DIR, "scaler.pickle")
ENCODER_PATH = os.path.join(MODEL_DIR, "encoder.pickle")

loaded_model = None
scaler = None
encoder = None

# Emotion labels mapping
EMOTION_LABELS = {
    0: 'neutral',
    1: 'calm', 
    2: 'happy',
    3: 'sad',
    4: 'angry',
    5: 'fearful',
    6: 'disgust',
    7: 'surprised'
}

def load_model_from_disk():
    """Load the emotion detection model, scaler, and encoder."""
    global loaded_model, scaler, encoder
    try:
        # Find available JSON and weights files
        json_path = None
        weights_path = None
        
        for path in MODEL_JSON_PATHS:
            if os.path.exists(path):
                json_path = path
                break
                
        for path in MODEL_WEIGHTS_PATHS:
            if os.path.exists(path):
                weights_path = path
                break
        
        # Check if JSON and weights files exist first (preferred method)
        if json_path and weights_path:
            print("📄 Loading model from JSON architecture + weights...")
            print(f"JSON file: {json_path}")
            print(f"Weights file: {weights_path}")
            
            # Load model architecture from JSON
            with open(json_path, 'r') as json_file:
                loaded_model_json = json_file.read()
            
            loaded_model = model_from_json(loaded_model_json)
            
            # Load weights
            loaded_model.load_weights(weights_path)
            
            # Compile the model
            loaded_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
            
            print("✓ Model loaded successfully from JSON + weights")
            
        # Fallback to complete H5 file
        elif os.path.exists(MODEL_H5_PATH):
            print("💾 Loading complete model from H5 file...")
            print(f"H5 file: {MODEL_H5_PATH}")
            
            loaded_model = tf.keras.models.load_model(MODEL_H5_PATH, compile=False)
            print("✓ Model loaded successfully from H5 file")
            
        else:
            error_msg = f"No model files found! Checked:\n- JSON paths: {MODEL_JSON_PATHS}\n- Weights paths: {MODEL_WEIGHTS_PATHS}\n- H5: {MODEL_H5_PATH}"
            print(error_msg)
            raise FileNotFoundError(error_msg)
        
        print(f"Model input shape: {loaded_model.input_shape}")
        
        # Load scaler
        if os.path.exists(SCALER_PATH):
            with open(SCALER_PATH, 'rb') as f:
                scaler = pickle.load(f)
            print("✓ Scaler loaded successfully")
        else:
            print("⚠️  Scaler not found, will skip scaling")
            
        # Load encoder
        if os.path.exists(ENCODER_PATH):
            with open(ENCODER_PATH, 'rb') as f:
                encoder = pickle.load(f)
            print("✓ Encoder loaded successfully")
        else:
            print("⚠️  Encoder not found, will use default labels")
        
    except Exception as e:
        print(f"Error loading model components: {e}")
        loaded_model = None
        scaler = None
        encoder = None
        raise e

def extract_features(data, sr=22050, frame_length=2048, hop_length=512):
    """Extract features exactly as in the notebook"""
    # Zero Crossing Rate
    zcr = librosa.feature.zero_crossing_rate(data, frame_length=frame_length, hop_length=hop_length)
    zcr = np.squeeze(zcr)
    
    # RMS Energy
    rmse = librosa.feature.rms(y=data, frame_length=frame_length, hop_length=hop_length)
    rmse = np.squeeze(rmse)
    
    # MFCCs
    mfcc = librosa.feature.mfcc(y=data, sr=sr)
    mfcc = np.ravel(mfcc.T)
    
    # Combine all features
    result = np.hstack((zcr, rmse, mfcc))
    return result

def get_features(file_path, duration=2.5, offset=0.6):
    """Get features with data augmentation exactly as in the notebook"""
    data, sr = librosa.load(file_path, duration=duration, offset=offset)
    
    # Original audio
    aud = extract_features(data)
    audio = np.array(aud)
    
    # Data augmentation (noise)
    noise_amp = 0.035 * np.random.uniform() * np.amax(data)
    noised_data = data + noise_amp * np.random.normal(size=data.shape[0])
    aud2 = extract_features(noised_data)
    audio = np.vstack((audio, aud2))
    
    # Data augmentation (pitch shift)
    pitched_data = librosa.effects.pitch_shift(data, sr=sr, n_steps=0.7)
    aud3 = extract_features(pitched_data)
    audio = np.vstack((audio, aud3))
    
    # Combined augmentation (pitch + noise)
    pitched_data1 = librosa.effects.pitch_shift(data, sr=sr, n_steps=0.7)
    noise_amp = 0.035 * np.random.uniform() * np.amax(pitched_data1)
    pitched_noised_data = pitched_data1 + noise_amp * np.random.normal(size=pitched_data1.shape[0])
    aud4 = extract_features(pitched_noised_data)
    audio = np.vstack((audio, aud4))
    
    return audio

def preprocess_audio(file_path: str) -> np.ndarray:
    """
    Preprocess audio file to extract features exactly matching the notebook pipeline.
    
    Args:
        file_path: Path to the audio file
        
    Returns:
        Preprocessed features as numpy array
    """
    # Get features with augmentation (returns 4 samples)
    features = get_features(file_path)
    
    # Use only the first (original) feature set for prediction
    X = features[0].reshape(1, -1)
    
    # Apply scaling if scaler is available
    if scaler is not None:
        X = scaler.transform(X)
    
    # Reshape for CNN model: (batch_size, features, 1)
    X = np.expand_dims(X, axis=2)
    
    return X

@app.on_event("startup") 
async def startup_event():
    """Load model on startup."""
    try:
        load_model_from_disk()
    except Exception as e:
        print(f"Failed to load model on startup: {e}")
        # Continue without model for debugging

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the main page."""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Emotion Detection from Audio</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                text-align: center;
                color: #333;
                margin-bottom: 30px;
            }
            .recording-section {
                margin: 20px 0;
                padding: 20px;
                border: 2px solid #ddd;
                border-radius: 8px;
                text-align: center;
            }
            button {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 10px 20px;
                margin: 5px;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            button:hover {
                background-color: #0056b3;
            }
            button:disabled {
                background-color: #ccc;
                cursor: not-allowed;
            }
            .record-btn {
                background-color: #dc3545;
            }
            .record-btn:hover {
                background-color: #c82333;
            }
            .upload-section {
                margin: 20px 0;
                padding: 20px;
                border: 2px solid #ddd;
                border-radius: 8px;
            }
            input[type="file"] {
                margin: 10px 0;
                padding: 5px;
            }
            .result {
                margin: 20px 0;
                padding: 20px;
                border-radius: 8px;
                text-align: center;
                font-size: 18px;
                font-weight: bold;
            }
            .result.success {
                background-color: #d4edda;
                color: #155724;
                border: 1px solid #c3e6cb;
            }
            .result.error {
                background-color: #f8d7da;
                color: #721c24;
                border: 1px solid #f5c6cb;
            }
            .loading {
                display: none;
                text-align: center;
                padding: 20px;
            }
            .spinner {
                border: 4px solid #f3f3f3;
                border-top: 4px solid #3498db;
                border-radius: 50%;
                width: 40px;
                height: 40px;
                animation: spin 2s linear infinite;
                margin: 0 auto;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎤 Emotion Detection from Audio</h1>
            
            <!-- Recording Section -->
            <div class="recording-section">
                <h3>Record Audio</h3>
                <p>Click to start recording your voice</p>
                <button id="recordBtn" class="record-btn">Start Recording</button>
                <button id="stopBtn" disabled>Stop Recording</button>
                <button id="playBtn" disabled>Play Recording</button>
                <div id="recordingStatus"></div>
                <audio id="audioPlayback" controls style="display:none; margin-top:10px;"></audio>
            </div>
            
            <!-- Upload Section -->
            <div class="upload-section">
                <h3>Or Upload Audio File</h3>
                <input type="file" id="fileInput" accept="audio/*">
                <button id="uploadBtn">Analyze Uploaded File</button>
            </div>
            
            <!-- Loading -->
            <div class="loading" id="loading">
                <div class="spinner"></div>
                <p>Analyzing audio...</p>
            </div>
            
            <!-- Result -->
            <div id="result"></div>
        </div>

        <script>
            let mediaRecorder;
            let audioChunks = [];
            let recordedBlob;

            const recordBtn = document.getElementById('recordBtn');
            const stopBtn = document.getElementById('stopBtn');
            const playBtn = document.getElementById('playBtn');
            const uploadBtn = document.getElementById('uploadBtn');
            const fileInput = document.getElementById('fileInput');
            const audioPlayback = document.getElementById('audioPlayback');
            const recordingStatus = document.getElementById('recordingStatus');
            const result = document.getElementById('result');
            const loading = document.getElementById('loading');

            // Initialize media recorder
            async function initRecorder() {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                    mediaRecorder = new MediaRecorder(stream);
                    
                    mediaRecorder.ondataavailable = event => {
                        audioChunks.push(event.data);
                    };
                    
                    mediaRecorder.onstop = () => {
                        recordedBlob = new Blob(audioChunks, { type: 'audio/wav' });
                        const audioUrl = URL.createObjectURL(recordedBlob);
                        audioPlayback.src = audioUrl;
                        audioPlayback.style.display = 'block';
                        playBtn.disabled = false;
                        
                        // Auto-analyze recorded audio
                        analyzeAudio(recordedBlob, 'recorded_audio.wav');
                    };
                } catch (error) {
                    console.error('Error accessing microphone:', error);
                    showResult('Error: Could not access microphone. Please check permissions.', 'error');
                }
            }

            // Recording controls
            recordBtn.onclick = () => {
                audioChunks = [];
                mediaRecorder.start();
                recordBtn.disabled = true;
                stopBtn.disabled = false;
                recordingStatus.textContent = 'Recording...';
                result.innerHTML = '';
            };

            stopBtn.onclick = () => {
                mediaRecorder.stop();
                recordBtn.disabled = false;
                stopBtn.disabled = true;
                recordingStatus.textContent = 'Recording stopped';
            };

            playBtn.onclick = () => {
                audioPlayback.play();
            };

            // Upload functionality
            uploadBtn.onclick = () => {
                const file = fileInput.files[0];
                if (file) {
                    analyzeAudio(file, file.name);
                } else {
                    showResult('Please select an audio file first.', 'error');
                }
            };

            // Analyze audio function
            async function analyzeAudio(audioFile, fileName) {
                const formData = new FormData();
                formData.append('file', audioFile, fileName);
                
                showLoading(true);
                result.innerHTML = '';
                
                try {
                    const response = await fetch('/predict', {
                        method: 'POST',
                        body: formData
                    });
                    
                    const data = await response.json();
                    
                    if (response.ok) {
                        showResult(`Detected Emotion: ${data.emotion.toUpperCase()}`, 'success');
                    } else {
                        showResult(`Error: ${data.detail}`, 'error');
                    }
                } catch (error) {
                    showResult(`Error: ${error.message}`, 'error');
                } finally {
                    showLoading(false);
                }
            }

            function showResult(message, type) {
                result.innerHTML = `<div class="result ${type}">${message}</div>`;
            }

            function showLoading(show) {
                loading.style.display = show ? 'block' : 'none';
            }

            // Initialize when page loads
            window.onload = () => {
                initRecorder();
            };
        </script>
    </body>
    </html>
    """

@app.post("/predict")
async def predict_emotion(file: UploadFile = File(...)) -> Dict[str, Union[str, float]]:
    """
    Predict emotion from uploaded audio file.
    
    Args:
        file: Uploaded audio file
        
    Returns:
        Dictionary containing the predicted emotion and confidence
    """
    if loaded_model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    # Validate file type
    if not file.content_type.startswith('audio/'):
        raise HTTPException(status_code=400, detail="File must be an audio file")
    
    # Create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        content = await file.read()
        temp_file.write(content)
        temp_file_path = temp_file.name
    
    try:
        # Preprocess audio
        features = preprocess_audio(temp_file_path)
        
        # Make prediction with TensorFlow 2.x
        probabilities = loaded_model.predict(features, verbose=0)
        predicted_class = np.argmax(probabilities, axis=1)[0]
        
        # Convert to emotion label using encoder if available
        if encoder is not None:
            # Use encoder to get the emotion label
            # Create one-hot encoded array for inverse transform
            predicted_one_hot = np.zeros((1, len(probabilities[0])))
            predicted_one_hot[0, predicted_class] = 1
            emotion = encoder.inverse_transform(predicted_one_hot)[0][0]
        else:
            # Fallback to default labels
            emotion = EMOTION_LABELS.get(predicted_class, "unknown")
        
        # Get confidence score
        confidence = float(probabilities[0][predicted_class])
        
        print(f"Predicted class: {predicted_class}, Emotion: {emotion}, Confidence: {confidence:.4f}")
        
        return {"emotion": emotion, "confidence": round(confidence, 4)}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing audio: {str(e)}")
    
    finally:
        # Clean up temporary file
        if os.path.exists(temp_file_path):
            os.unlink(temp_file_path)

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "model_loaded": loaded_model is not None}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)