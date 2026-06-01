from flask import Flask, request, jsonify, render_template, redirect
import requests

app = Flask(__name__)

CURRENCY_MANAGER = "http://localhost:5001"
DATA_MANAGER = "http://localhost:5002"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load', methods=['POST'])
def proxy_load():
    data = request.get_json()
    resp = requests.post(f"{CURRENCY_MANAGER}/load", json=data)
    return resp.text, resp.status_code

@app.route('/update_currency', methods=['POST'])
def proxy_update():
    data = request.get_json()
    resp = requests.post(f"{CURRENCY_MANAGER}/update_currency", json=data)
    return resp.text, resp.status_code

@app.route('/delete', methods=['POST'])
def proxy_delete():
    data = request.get_json()
    resp = requests.post(f"{CURRENCY_MANAGER}/delete", json=data)
    return resp.text, resp.status_code

@app.route('/convert', methods=['GET'])
def proxy_convert():
    currency = request.args.get('currency')
    amount = request.args.get('amount')
    resp = requests.get(f"{DATA_MANAGER}/convert?currency={currency}&amount={amount}")
    return resp.text, resp.status_code

@app.route('/currencies_page')
def currencies_page():
    resp = requests.get(f"{DATA_MANAGER}/currencies")
    currencies = resp.json()
    return render_template('currencies.html', currencies=currencies)

@app.route('/convert_page')
def convert_page():
    return render_template('convert.html')

if __name__ == '__main__':
    app.run(port=5000)