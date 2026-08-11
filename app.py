from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('data.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, email TEXT, mobile NUM)')
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']

        conn = sqlite3.connect('data.db')
        conn.execute('INSERT INTO users (name, email, mobile) VALUES (?, ?, ?)', (name, email, mobile))
        conn.commit()
        conn.close()

    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
