document.getElementById('darkModeToggle').addEventListener('click', () => {
    document.body.classList.toggle('dark');
});
document.getElementById('predictBtn').addEventListener('click', () => {
    let duration = parseInt(document.getElementById('duration').value) || 200;
    let stops = parseInt(document.getElementById('stops').value) || 1;
    let price = 2500 + duration * 5 + stops * 1000;
    document.getElementById('result').innerText = `💰 Estimated Price: ₹ ${price}`;
});