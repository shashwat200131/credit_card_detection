from flask import Flask, request, jsonify, render_template
from luhn_algorithm import luhn_algorithm

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    card_number = data.get('card_number')  # Ensure this key matches with JS
    if card_number and luhn_algorithm(card_number):
        return jsonify(message='Valid credit card number!')
    else:
        return jsonify(message='Invalid credit card number.')

if __name__ == '__main__':
    app.run(debug=True)
