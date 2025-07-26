document.getElementById('predictBtn').addEventListener('click', async () => {
    let duration = parseInt(document.getElementById('duration').value) || 200;
    let stops = parseInt(document.getElementById('stops').value) || 1;

    let response = await fetch("https://travel-api-1zx0.onrender.com/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ duration: duration, stops: stops })
    });

    let result = await response.json();
    document.getElementById('result').innerText = `💰 Estimated Price: ₹ ${result.predicted_price.toFixed(2)}`;
});
