from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_real_rate(currency):
    try:
        url = f"https://api.frankfurter.dev/v2/rate/{currency}/RUB"
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            return resp.json().get('rate')
    except Exception as e:
        print(f"Frankfurter error: {e}")
    return None

@app.route('/rate')
def get_rate():
    currency = request.args.get('currency')
    
    if not currency:
        return jsonify({'message': 'CURRENCY PARAMETER REQUIRED'}), 400
    
    if currency not in ('USD', 'EUR'):
        return jsonify({'message': 'UNKNOWN CURRENCY'}), 400
    
    real_rate = get_real_rate(currency)
    if real_rate:
        return jsonify({'rate': real_rate})
    
    # Если Frankfurter не работает
    static_rates = {'USD': 71.0, 'EUR': 82.0}
    return jsonify({'rate': static_rates[currency]})

if __name__ == '__main__':
    app.run(port=5001, debug=True)