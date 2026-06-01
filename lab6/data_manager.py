from flask import Flask, request, jsonify
import psycopg2
import requests

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="currenciesbd",
    user="postgres",
    password="123"
)
cur = conn.cursor()

@app.route('/convert', methods=['GET'])
def convert():
    currency = request.args.get('currency')
    amount = float(request.args.get('amount'))
    
    cur.execute("SELECT rate FROM currencies WHERE currency_name = %s", (currency,))
    row = cur.fetchone()
    if not row:
        return "Валюта не найдена", 404
    
    rate = row[0]
    result = amount * rate
    
    return jsonify({"converted_amount": result})

@app.route('/currencies', methods=['GET'])
def get_currencies():
    cur.execute("SELECT currency_name, rate FROM currencies")
    rows = cur.fetchall()
    
    currencies_list = []
    for row in rows:
        currencies_list.append({
            "currency_name": row[0],
            "rate": row[1]
        })
    
    return jsonify(currencies_list)

if __name__ == '__main__':
    app.run(port=5002)