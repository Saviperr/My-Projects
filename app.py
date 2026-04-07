import os
import time
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'mysql')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'devuser')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'devpass')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'devops')

mysql = MySQL(app)

def init_db():
    time.sleep(10)
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            message TEXT
        );
        """)
        mysql.connection.commit()
        cur.close()

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute('SELECT message FROM messages')
    messages = cur.fetchall()
    cur.close()
    return render_template('index.html', messages=messages)

@app.route('/submit', methods=['POST'])
def submit():
    msg = request.form.get('new_message')
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO messages (message) VALUES (%s)', [msg])
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': msg})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
