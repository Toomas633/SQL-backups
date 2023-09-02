from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
import sqlite3

app = Flask(__name__, template_folder='web/')
app.secret_key = '$2b$12$R0hxaE9n7B.r5ls7UnFBC.tLtsO0h/CrhYyW4kLdeyR5XhTI11Pv.'
bcrypt = Bcrypt(app)


def get_password(username):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE user = ?', (username,))
    password = cursor.fetchone()
    cursor.close()
    return password[0] if password else False


@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = get_password(username)
        if password_hash is not False:
            if bcrypt.check_password_hash(password_hash, password):
                session['username'] = username
                return redirect(url_for('dashboard'))
            else:
                return redirect(url_for('login', message='ERROR: Wrong password'))
        else:
            return redirect(url_for('login', message='ERROR: No user found'))

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
