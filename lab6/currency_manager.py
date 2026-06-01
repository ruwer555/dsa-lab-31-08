from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="currenciesbd",
    user="postgres",
    password="123"
)
cur = conn.cursor() 

@app.route('/load', methods=['POST'])
def load():
    data = request.get_json()
    name = data['currency_name']
    rate = data['rate']
    
    cur.execute("SELECT * FROM currencies WHERE currency_name = %s", (name,))
    if cur.fetchone():
        return "Валюта уже существует", 400
    
    cur.execute("INSERT INTO currencies (currency_name, rate) VALUES (%s, %s)", (name, rate))
    conn.commit()
    return "OK", 200

@app.route('/update_currency', methods=['POST'])
def update():
    data = request.get_json()
    name = data['currency_name']
    rate = data['rate']
    
    cur.execute("SELECT * FROM currencies WHERE currency_name = %s", (name,))
    if not cur.fetchone():
        return "Валюта не найдена", 404
    
    cur.execute("UPDATE currencies SET rate = %s WHERE currency_name = %s", (rate, name))
    conn.commit()
    return "OK", 200

@app.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()
    name = data['currency_name']
    
    cur.execute("SELECT * FROM currencies WHERE currency_name = %s", (name,))
    if not cur.fetchone():
        return "Валюта не найдена", 404
    
    cur.execute("DELETE FROM currencies WHERE currency_name = %s", (name,))
    conn.commit()
    return "OK", 200

if __name__ == '__main__':
    app.run(port=5001)