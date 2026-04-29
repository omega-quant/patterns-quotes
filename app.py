from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# DB setup
def init_db():
    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Get all quotes
@app.route('/get_quotes')
def get_quotes():
    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()
    c.execute("SELECT text FROM quotes")
    data = c.fetchall()
    conn.close()

    return jsonify([q[0] for q in data])

# Add quote
@app.route('/add_quote', methods=['POST'])
def add_quote():
    data = request.json
    text = data.get('text')

    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()
    c.execute("INSERT INTO quotes (text) VALUES (?)", (text,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Quote added"})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def home():
    return render_template('index.html')

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

@app.route('/test')
def test():
    return "Hello from backend"
