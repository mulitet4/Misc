<script>
	import { onMount } from 'svelte';
	import * as tf from '@tensorflow/tfjs';

	let canvas;
	let ctx;
	const canvasColor = 'black';
	const lineWidth = 15;
	const strokeColor = 'yellow';

	let mouseX,
		mouseY,
		lastX,
		lastY,
		isMouseDown = false;
	let touchX, touchY;
	let isResultDivPresent = false;
	let model;
	let predictions = Array(10).fill(0);
	let maxIndex = null;
	let maxElement = 0;
	let confidence = 0;

	onMount(async () => {
		initCanvas();
		await loadModel();
	});

	async function loadModel() {
		try {
			// Replace this URL with your actual model URL
			model = await tf.loadLayersModel('/model/model.json');

			console.log('Model loaded successfully');
		} catch (error) {
			console.error('Failed to load model:', error);
		}
	}

	function initCanvas() {
		if (!canvas) return;

		ctx = canvas.getContext('2d');
		ctx.fillStyle = canvasColor;
		ctx.fillRect(0, 0, canvas.width, canvas.height);
		console.log('Canvas initialized:', canvas.width, canvas.height);
	}

	function drawWithMouse(ctx, x, y, size, isDown) {
		if (isDown) {
			ctx.beginPath();
			ctx.strokeStyle = strokeColor;
			ctx.lineWidth = lineWidth;
			ctx.lineJoin = ctx.lineCap = 'round';
			ctx.moveTo(lastX, lastY);
			ctx.lineTo(x, y);
			ctx.closePath();
			ctx.stroke();
		}
		lastX = x;
		lastY = y;
	}

	function handleMouseDown(event) {
		isMouseDown = true;
		getMousePos(event);
		lastX = mouseX;
		lastY = mouseY;
		drawWithMouse(ctx, mouseX, mouseY, 12, false);
	}

	async function handleMouseUp(event) {
		isMouseDown = false;
		if (!model) return;

		let tensor = preprocessCanvas(canvas);
		let predictionResults = await model.predict(tensor).data();
		predictions = Array.from(predictionResults);
		displayResults();
	}

	function handleMouseMove(event) {
		getMousePos(event);
		if (isMouseDown) {
			drawWithMouse(ctx, mouseX, mouseY, 12, true);
		}
	}

	function getMousePos(event) {
		if (event.offsetX) {
			mouseX = event.offsetX;
			mouseY = event.offsetY;
		} else if (event.layerX) {
			mouseX = event.layerX;
			mouseY = event.layerY;
		}
	}

	function handleTouchStart(event) {
		getTouchPos(event);
		lastX = touchX;
		lastY = touchY;
		drawWithMouse(ctx, touchX, touchY, 12, false);
		event.preventDefault();
	}

	function handleTouchMove(event) {
		getTouchPos(event);
		drawWithMouse(ctx, touchX, touchY, 12, true);
		event.preventDefault();
	}

	function getTouchPos(event) {
		if (event.touches && event.touches.length == 1) {
			const touch = event.touches[0];
			touchX = touch.pageX - touch.target.offsetLeft;
			touchY = touch.pageY - touch.target.offsetTop;
		}
	}

	function clearCanvas() {
		if (!ctx) return;
		ctx.clearRect(0, 0, canvas.width, canvas.height);
		ctx.fillStyle = canvasColor;
		ctx.fillRect(0, 0, canvas.width, canvas.height);
		predictions = Array(10).fill(0);
		maxIndex = null;
		maxElement = 0;
		confidence = 0;
		isResultDivPresent = false;
	}

	function preprocessCanvas(image) {
		let tensor = tf.browser
			.fromPixels(image)
			.resizeNearestNeighbor([28, 28])
			.mean(2)
			.expandDims(2)
			.expandDims()
			.toFloat();
		return tensor.div(255.0);
	}

	function displayResults() {
		maxElement = Math.max(...predictions);
		maxIndex = predictions.indexOf(maxElement);
		confidence = (maxElement * 100).toFixed(2);
		isResultDivPresent = true;
		console.log(`Prediction: ${maxIndex}, Confidence: ${confidence}%`);
	}
</script>

<svelte:head>
	<title>Digit Recognition</title>
	<script src="https://cdn.tailwindcss.com"></script>
</svelte:head>

<div class="min-h-screen bg-slate-100 py-8 px-4">
	<div class="max-w-4xl mx-auto">
		<!-- Header -->
		<div class="text-center mb-6">
			<h1 class="text-3xl font-semibold text-slate-800">
				Handwritten <span class="text-blue-600">Digit Recognition</span>
			</h1>
			<p class="text-slate-500 mt-2">Draw a digit (0-9) and let the AI predict it</p>
		</div>

		<!-- Main Content -->
		<div class="bg-white rounded-lg shadow-md p-6">
			<div class="flex flex-col lg:flex-row gap-6">
				<!-- Canvas Section -->
				<div class="flex-1">
					<div class="flex flex-col items-center">
						<canvas
							bind:this={canvas}
							id="sketchpad"
							height="280"
							width="280"
							class="border-2 border-slate-300 rounded-md shadow-sm bg-black"
							on:mousedown={handleMouseDown}
							on:mousemove={handleMouseMove}
							on:mouseup={handleMouseUp}
							on:touchstart={handleTouchStart}
							on:touchmove={handleTouchMove}
							on:touchend={handleMouseUp}
						></canvas>
						<div class="mt-4 flex space-x-3">
							<button 
								type="button" 
								class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded text-sm transition-colors duration-200"
								on:click={clearCanvas}
							>
								Clear Canvas
							</button>
						</div>
					</div>
				</div>

				<!-- Predictions Column -->
				<div class="flex-1">
					<div class="mb-4">
						<h2 class="text-lg font-medium text-slate-700 mb-2">Prediction Scores</h2>
						<div class="bg-slate-50 rounded border border-slate-200">
							<div class="grid grid-cols-5 gap-1 p-2">
								{#each Array(10) as _, i}
									<div class={`text-center rounded py-1 ${maxIndex === i ? 'bg-blue-100 border border-blue-300' : ''}`}>
										<div class="text-lg font-medium text-slate-800">{i}</div>
										<div class="text-xs text-slate-500">{predictions[i] ? predictions[i].toFixed(2) : '0.00'}</div>
									</div>
								{/each}
							</div>
						</div>
					</div>

					{#if isResultDivPresent}
						<div class="mt-6 bg-slate-50 rounded-md p-4 border border-slate-200">
							<div class="flex justify-between items-center">
								<div>
									<div class="text-sm text-slate-500">Prediction</div>
									<div class="text-3xl font-bold text-blue-600">{maxIndex}</div>
								</div>
								<div>
									<div class="text-sm text-slate-500">Confidence</div>
									<div class="text-3xl font-bold text-blue-600">{confidence}%</div>
								</div>
							</div>
							<div class="w-full bg-slate-200 rounded-full h-2 mt-4">
								<div class="bg-blue-600 h-2 rounded-full" style="width: {confidence}%"></div>
							</div>
						</div>
					{/if}

					<div class="mt-6">
						<h3 class="text-lg font-medium text-slate-700 mb-2">How It Works</h3>
						<p class="text-sm text-slate-600">
							This application uses a trained neural network to recognize handwritten digits. Draw a number from 0-9 on the canvas, and the model will predict which digit you've drawn.
						</p>
					</div>
				</div>
			</div>
		</div>

		<!-- Footer -->
		<div class="mt-6 text-center text-slate-500 text-xs">
			<p></p>
		</div>
	</div>
</div>