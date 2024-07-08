document.getElementById('card-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const cardNumber = document.getElementById('card-number').value;

    fetch('/validate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ card_number: cardNumber }) // Note: 'card_number' key
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = data.message;
    })
    .catch(error => console.error('Error:', error));
});
