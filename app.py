from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    produits = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return render_template('index.html', produits=produits)

@app.route('/ajouter', methods=('GET', 'POST'))
def ajouter():
    if request.method == 'POST':
        nom = request.form['nom']
        description = request.form['description']
        quantite = request.form['quantite']
        prix = request.form['prix']
        conn = get_db_connection()
        conn.execute('INSERT INTO products (nom, description, quantité, prix_unitaire) VALUES (?, ?, ?, ?)',
                     (nom, description, quantite, prix))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_product.html')
