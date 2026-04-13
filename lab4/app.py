from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
app.secret_key = 'super-secret-key-2026'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

def get_db():
    return psycopg2.connect(
        host="localhost",
        database="dev_lab4_31_08",
        user="postgres",
        password="123",
        port="5432"
    )

class User(UserMixin):
    def __init__(self, id, email, password, name):
        self.id = str(id)
        self.email = email
        self.password = password
        self.name = name

@login_manager.user_loader
def load_user(user_id):
    with get_db() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            u = cur.fetchone()
            return User(u['id'], u['email'], u['password'], u['name']) if u else None

@app.route('/')
def index():
    return render_template('index.html', name=current_user.name) if current_user.is_authenticated else redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        with get_db() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM users WHERE email = %s", (request.form['email'],))
                u = cur.fetchone()
        if u and check_password_hash(u['password'], request.form['password']):
            login_user(User(u['id'], u['email'], u['password'], u['name']))
            return redirect(url_for('index'))
        return render_template('login.html', error='Неверный email или пароль')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        with get_db() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE email = %s", (request.form['email'],))
                if cur.fetchone():
                    return render_template('signup.html', error='Email уже существует')
                cur.execute("INSERT INTO users (email, password, name) VALUES (%s, %s, %s)",
                           (request.form['email'], generate_password_hash(request.form['password']), request.form['name']))
                conn.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))