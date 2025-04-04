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
	<link href="https://fonts.googleapis.com/css?family=Niconne" rel="stylesheet" />
	<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Audiowide" />
	<link
		href="https://fonts.googleapis.com/css?family=Calistoga|Josefin+Sans:400,700|Pacifico&display=swap"
		rel="stylesheet"
	/>
	<link
		rel="stylesheet"
		href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
	/>
</svelte:head>

<div class="sketchpadapp container">
	<div class="row justify-content-md-center">
		<section id="title">
			<h1 class="heading">Handwritten <span class="heading-sp">Digit Recognition</span></h1>
		</section>
	</div>

	<div class="row">
		<div class="col-lg-6 col-md-6 col-sm-12">
			<canvas
				bind:this={canvas}
				id="sketchpad"
				height="350"
				width="350"
				on:mousedown={handleMouseDown}
				on:mousemove={handleMouseMove}
				on:mouseup={handleMouseUp}
				on:touchstart={handleTouchStart}
				on:touchmove={handleTouchMove}
				on:touchend={handleMouseUp}
			></canvas>
			<div class="buttons_div">
				<button type="button" class="btn btn-warning" on:click={clearCanvas}
					>&nbsp Clear &nbsp</button
				>
			</div>
		</div>

		<div class="col-lg-6 col-md-6 col-sm-12">
			<table class="table-sm table-striped table-borderless table">
				<thead>
					<tr>
						<th scope="col">Digit</th>
						<th scope="col">Score</th>
					</tr>
				</thead>
				<tbody>
					{#each Array(10) as _, i}
						<tr>
							<th class={maxIndex === i ? 'answer' : ''}>{i}</th>
							<td class={maxIndex === i ? 'answer' : ''}>
								{predictions[i] ? predictions[i].toFixed(2) : ''}
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</div>

	{#if isResultDivPresent}
		<div class="row" id="result">
			<div class="col-lg-6 col-md-6 col-sm-12">
				<h2 id="prediction_heading" class="prediction">
					Prediction:
					<span class="score">{maxIndex}</span>
				</h2>
			</div>
			<div class="col-lg-6 col-md-6 col-sm-12">
				<h2 id="confidence" class="prediction">
					Confidence:
					<span class="score">{confidence}%</span>
				</h2>
			</div>
		</div>
	{/if}
</div>

<style>
	.prediction {
		font-family: 'Josefin Sans', sans-serif;
		margin-top: 7.5%;
	}
	.score {
		color: #4caf50;
		font-weight: bold;
	}
	.answer {
		background-color: #4caf50;
		font-weight: bold;
	}
	#confidence {
		font-family: 'Josefin Sans', sans-serif;
		margin-top: 7.5%;
	}
	#result {
		font-family: 'Pacifico', cursive;
		font-size: 5rem;
	}
	#sketchpad {
		border: 2px solid #888;
		border-radius: 4px;
	}
	#title {
		padding: 1.5% 15%;
		margin: 0 auto;
		text-align: center;
	}
	:global(body) {
		overflow: hidden;
	}
	.buttons_div {
		margin-top: 10px;
	}
	.heading {
		width: 50vw;
		text-align: center;
		position: relative;
		color: white;
		background-color: #6871b1;
		padding-top: 1%;
		padding-bottom: 1%;
		font-family: 'Audiowide', sans-serif;
	}
	.heading-sp {
		color: yellow;
	}
	:global(table.result > tbody > tr:nth-child(odd)) {
		background-color: mistyrose;
	}
	:global(table.result > tbody > tr:first-child) {
		background-color: white;
	}
	:global(table.result > tbody > tr > td) {
		border-radius: 0;
	}
	:global(table th, td) {
		border: none;
		padding: 5px;
		text-align: center;
	}
</style>
