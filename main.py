from flask import Flask, render_template, g
import sqlite3

from auth import auth_bp            
from categorias import categorias_bp 
from carrito import carrito_bp      

app = Flask(__name__)
app.secret_key = 'clave_secreta_masusu_shop'
DATABASE = 'masusuDatabase.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Registras todos tus Blueprints de manera ordenada
app.register_blueprint(auth_bp)
app.register_blueprint(categorias_bp)
app.register_blueprint(carrito_bp) 

# Ruta para el menú principal (con consulta de 16 productos variados)
@app.route('/')
@app.route('/menu')
def menu_principal():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM productos ORDER BY RANDOM() LIMIT 16")
    productos = cursor.fetchall()
    return render_template('MenuPrincipal.html', productos=productos)

# Ruta para el login de usuarios
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)