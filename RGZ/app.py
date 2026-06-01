import hashlib
import requests
from flask import Flask, request, jsonify, render_template, redirect, session
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
app.secret_key = 'secret-key'

DB_NAME = 'RGZ_RPP_DB'
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_HOST = 'localhost'

def get_db_connection():
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST,
        cursor_factory=RealDictCursor
    )

@app.route('/reg', methods=['POST'])
def register():
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')
    if not login or not password:
        return jsonify({'error': 'login and password required'}), 500
    hashed = hashlib.sha256(password.encode()).hexdigest()
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO users (name, password) VALUES (%s, %s)', (login, hashed))
        conn.commit()
    except:
        return jsonify({'error': 'user already exists'}), 500
    finally:
        cur.close()
        conn.close()
    return jsonify({'status': 'ok'}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')
    hashed = hashlib.sha256(password.encode()).hexdigest()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id FROM users WHERE name = %s AND password = %s', (login, hashed))
    user = cur.fetchone()
    cur.close()
    conn.close()
    if user:
        session['user_id'] = user['id']
        return jsonify({'status': 'ok'}), 200
    return jsonify({'error': 'invalid credentials'}), 500

@app.route('/add_operation', methods=['GET', 'POST'])
def add_operation():
    if 'user_id' not in session:
        return redirect('/login_page')
    if request.method == 'GET':
        return render_template('add_operation.html')
    user_id = session['user_id']
    date_str = request.form['date']
    sum_val = float(request.form['sum'])
    type_op = request.form['type_operation']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO operations (user_id, date, sum, type_operation) VALUES (%s, %s, %s, %s)',
        (user_id, date_str, sum_val, type_op)
    )
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/operations')


def get_exchange_rate(currency):
    """Возвращает курс RUB к USD или EUR через rate_service.py"""
    if currency == 'RUB':
        return 1
    
    try:
        url = f"http://localhost:5001/rate?currency={currency}"
        resp = requests.get(url, timeout=3)
        if resp.status_code == 200:
            return resp.json()['rate']
        else:
            print(f"Rate service error: {resp.status_code}")
    except Exception as e:
        print(f"Rate service exception: {e}")

@app.route('/operations')
def operations():
    if 'user_id' not in session:
        return redirect('/login_page')
    user_id = session['user_id']
    currency = request.args.get('currency', 'RUB')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM operations WHERE user_id = %s ORDER BY date DESC', (user_id,))
    ops = cur.fetchall()
    cur.close()
    conn.close()
    rate = 1
    if currency == 'EUR' or currency == 'USD':
        rate = get_exchange_rate(currency)
        if not rate:
            rate = 1
    total_income = 0
    total_expense = 0
    for op in ops:
        op_sum = float(op['sum']) / rate
        op['sum_converted'] = round(op_sum, 2)
        if op['type_operation'] == 'income':
            total_income += op_sum
        else:
            total_expense += op_sum
    return render_template('operations.html', operations=ops, currency=currency,
                           total_income=round(total_income, 2),
                           total_expense=round(total_expense, 2))

@app.route('/login_page')
def login_page():
    return render_template('login.html')

@app.route('/register_page')
def register_page():
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login_page')

@app.route('/')
def index():
    return redirect('/login_page')

if __name__ == '__main__':
    app.run(debug=True, port=5000)