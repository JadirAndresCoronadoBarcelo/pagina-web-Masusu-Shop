from flask import Blueprint, render_template, g
import sqlite3

# Creamos un Blueprint para las categorías
categorias_bp = Blueprint('categorias', __name__)
DATABASE = 'masusuDatabase.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@categorias_bp.teardown_request
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Ruta para Mouses
@categorias_bp.route('/categoria/mouses')
def categoria_mouses():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM productos WHERE categoria = ? LIMIT 16", ('Mouses',))
    productos = cursor.fetchall()
    return render_template('categoriaMouses.html', productos=productos)

# Ruta para Teclados
@categorias_bp.route('/categoria/teclados')
def categoria_teclados():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM productos WHERE categoria = ? LIMIT 16", ('Teclados',))
    productos = cursor.fetchall()
    return render_template('categoriaTeclados.html', productos=productos)

# Ruta para Diademas
@categorias_bp.route('/categoria/diademas')
def categoria_diademas():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM productos WHERE categoria = ? LIMIT 16", ('Diademas',))
    productos = cursor.fetchall()
    return render_template('categoriaDiademas.html', productos=productos)

# Ruta para Sillas
@categorias_bp.route('/categoria/sillas')
def categoria_sillas():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM productos WHERE categoria = ? LIMIT 16", ('Sillas',))
    productos = cursor.fetchall()
    return render_template('categoriaSillas.html', productos=productos)

# Reemplaza o ajusta esta ruta dentro de tu archivo categorias.py
@categorias_bp.route('/producto/<int:id_producto>')
def producto_vista(id_producto):
    db = get_db()
    cursor = db.cursor()
    
    # 1. Buscar el producto exacto por su ID
    cursor.execute("SELECT * FROM productos WHERE id_producto = ?", (id_producto,))
    producto = cursor.fetchone()
    
    if not producto:
        return "Producto no encontrado", 404
        
    # 2. (Opcional pero recomendado) Buscar 4 productos de la misma categoría para las tarjetas de abajo
    cursor.execute("SELECT * FROM productos WHERE categoria = ? AND id_producto != ? LIMIT 4", (producto['categoria'], id_producto))
    relacionados = cursor.fetchall()
    
    # Renderizar la vista pasando el producto principal y los relacionados
    return render_template('productoVista.html', producto=producto, relacionados=relacionados)