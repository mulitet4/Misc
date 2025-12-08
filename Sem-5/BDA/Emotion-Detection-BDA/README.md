# Speech Emotion Recognition using Apache Spark

This implementation demonstrates a distributed big data analytics approach to speech emotion recognition using Apache Spark and PySpark. The system processes large-scale audio datasets across four emotional speech corpora: **CREMA-D**, **RAVDESS**, **SAVEE**, and **TESS**, utilizing distributed computing for scalable machine learning model training and evaluation.

## System Architecture

### Distributed Computing Framework

- **Apache Spark**: Distributed processing engine for large-scale data analytics
- **PySpark**: Python API for Spark enabling machine learning at scale
- **HDFS**: Hadoop Distributed File System for scalable audio data storage
- **Spark ML**: Machine learning library for distributed model training

### Configuration Management

The system utilizes centralized configuration parameters for:

- Spark cluster settings (executor memory, cores, partitions)
- Feature extraction parameters (MFCC coefficients, frame lengths)
- Model hyperparameters (Random Forest, Multilayer Perceptron)
- Memory optimization settings for efficient processing

## Datasets

The system processes four large-scale emotional speech datasets stored in HDFS:

- **CREMA-D**: Crowd-sourced Emotional Multimodal Actors Dataset with 7,442 clips from 91 actors
- **RAVDESS**: Ryerson Audio-Visual Database of Emotional Speech and Song with 24 professional actors
- **SAVEE**: Surrey Audio-Visual Expressed Emotion database with four native English male speakers
- **TESS**: Toronto Emotional Speech Set with 2,800 audio files from two actresses

## Distributed Data Processing

### Data Ingestion

- Utilizes Spark RDDs for distributed file loading from HDFS
- Implements parallel processing across multiple executors
- Handles large-scale audio file metadata extraction

### Preprocessing Pipeline

- Distributed emotion label mapping across datasets
- Spark DataFrame operations for data integration
- Automated data quality checks and validation

### Feature Extraction

- **MFCC (Mel-frequency cepstral coefficients)**: 13 coefficients per frame
- **Zero Crossing Rate**: Temporal audio characteristics
- **RMS Energy**: Root Mean Square energy computation
- **Distributed Processing**: Feature extraction across Spark cluster nodes

## Data Augmentation at Scale

Implemented using Spark UDFs for distributed augmentation:

- **Noise Addition**: Gaussian noise injection with configurable factors
- **Audio Stretching**: Time-domain modifications
- **Pitch Shifting**: Frequency domain transformations
- **Temporal Shifting**: Time-based audio modifications

## Machine Learning Models

### Distributed Algorithms

- **Random Forest Classifier**: Distributed ensemble method with configurable trees and depth
- **Multilayer Perceptron**: Neural network implementation in Spark ML
- **Cross-Validation**: K-fold validation across distributed datasets

### Model Configuration

- **Random Forest**: 20 trees, max depth 5, optimized for memory efficiency
- **MLP**: Multi-layer architecture with configurable hidden layers
- **Hyperparameter Tuning**: Grid search using Spark ML pipelines

## Performance Optimization

### Memory Management

- Configurable partition strategies for optimal resource utilization
- Sampling techniques to prevent out-of-memory conditions
- Adaptive query execution for dynamic optimization

### Scalability Features

- Horizontal scaling across cluster nodes
- Fault-tolerant processing with automatic recovery
- Dynamic resource allocation based on workload

## Model Deployment

### Production Pipeline

- Complete ML pipeline with preprocessing, scaling, and classification
- Model serialization for distributed deployment
- Metadata storage for model versioning and configuration

### Deployment Artifacts

- Trained Random Forest and MLP models
- Feature scaling transformers
- Label indexers for emotion mapping
- Complete end-to-end prediction pipeline

## Results and Evaluation

### Model Performance

Performance evaluation using standard classification metrics:

- **Accuracy**: Multi-class classification accuracy
- **F1-Score**: Weighted F1-score across emotion classes
- **Precision and Recall**: Per-class performance metrics
- **Confusion Matrix**: Detailed classification analysis

### Distributed Evaluation

- Cross-validation performed across distributed datasets
- Model comparison between Random Forest and MLP algorithms
- Performance visualization and statistical analysis

## System Requirements

### Cluster Configuration

- **Minimum**: 4 executor nodes with 4GB memory each
- **Recommended**: 8+ executor nodes with 8GB+ memory
- **Storage**: HDFS cluster for audio dataset storage
- **Network**: High-bandwidth interconnect for data transfer

### Software Dependencies

- Apache Spark 3.x
- Python 3.7+
- PySpark ML libraries
- Librosa for audio processing
- NumPy, Pandas for data manipulation

## Execution Instructions

### Cluster Setup

1. Configure Hadoop HDFS cluster for data storage
2. Initialize Spark cluster with appropriate memory settings
3. Upload audio datasets to HDFS using configured paths

### Data Processing

1. Execute data ingestion cells to load datasets from HDFS
2. Run preprocessing pipeline for data integration and cleaning
3. Perform distributed feature extraction across cluster nodes

### Model Training

1. Configure Spark session with optimized memory settings
2. Execute distributed model training for Random Forest and MLP
3. Perform hyperparameter tuning using cross-validation

### Model Evaluation

1. Run model evaluation on distributed test datasets
2. Generate performance metrics and confusion matrices
3. Save trained models and pipeline artifacts

## Output Structure

```
output/
├── combined_audio_paths/          # Integrated dataset metadata
├── emotion_features_spark/        # Extracted feature vectors
├── emotion_labels_spark/          # Emotion label mappings
└── spark_ml_models/              # Trained models and pipelines
    ├── mlp_emotion_model/        # Multilayer Perceptron model
    ├── random_forest_emotion_model/ # Random Forest model
    ├── feature_scaler/           # Feature scaling transformer
    ├── label_indexer/            # Label indexing transformer
    ├── complete_emotion_pipeline/ # End-to-end pipeline
    ├── model_metadata.json       # Model performance metadata
    └── deployment_config.json    # Deployment configuration
```

This implementation demonstrates scalable machine learning techniques for emotion recognition in speech data, utilizing distributed computing principles for handling large-scale audio datasets efficiently.
