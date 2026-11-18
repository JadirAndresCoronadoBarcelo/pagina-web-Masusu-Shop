from flask import Blueprint, request, redirect, url_for, session, render_template, g
import sqlite3

# Creamos el Blueprint para el carrito
carrito_bp = Blueprint('carrito', __name__)
DATABASE = 'masusuDatabase.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@carrito_bp.teardown_request
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Ruta para ver el carrito de compras
@carrito_bp.route('/carrito')
def ver_carrito():
    if not session.get('id_usuario'):
        return redirect(url_for('login'))
        
    id_usuario = session['id_usuario']
    db = get_db()
    cursor = db.cursor()
    
    # Buscar el carrito único del usuario
    cursor.execute("SELECT id_carrito FROM carritos WHERE id_usuario = ?", (id_usuario,))
    carrito = cursor.fetchone()
    
    productos_carrito = []
    total_carrito = 0
    
    if carrito:
        id_carrito = carrito['id_carrito']
        # Consultar los ítems unidos a la tabla productos para traer nombres, imágenes, precios y subtotales
        cursor.execute("""
            SELECT ci.cantidad, ci.subTotal, p.id_producto, p.producto, p.precio, p.imagen 
            FROM carritoItems ci
            JOIN productos p ON ci.id_producto = p.id_producto
            WHERE ci.id_carrito = ?
        """, (id_carrito,))
        productos_carrito = cursor.fetchall()
        
        # Calcular el monto total del carrito
        for item in productos_carrito:
            total_carrito += item['subTotal']
            
    return render_template('carrito.html', productos=productos_carrito, total_carrito=total_carrito)

# Ruta para procesar la adición de un producto al carrito (POST) con validación de stock
@carrito_bp.route('/carrito/agregar/<int:id_producto>', methods=['POST'])
def agregar_carrito(id_producto):
    if not session.get('id_usuario'):
        return redirect(url_for('login'))
        
    id_usuario = session['id_usuario']
    cantidad_solicitada = int(request.form.get('cantidad', 1))
    
    db = get_db()
    cursor = db.cursor()
    
    # Consultamos tanto el precio como el stock disponible ('cantidad')
    cursor.execute("SELECT precio, cantidad FROM productos WHERE id_producto = ?", (id_producto,))
    producto = cursor.fetchone()
    if not producto:
        return "Producto no encontrado", 404
        
    precio_unitario = producto['precio']
    stock_disponible = producto['cantidad']
    
    # Buscar o crear carrito único por usuario
    cursor.execute("SELECT id_carrito FROM carritos WHERE id_usuario = ?", (id_usuario,))
    carrito = cursor.fetchone()
    
    if carrito:
        id_carrito = carrito['id_carrito']
    else:
        cursor.execute("INSERT INTO carritos (id_usuario) VALUES (?)", (id_usuario,))
        db.commit()
        id_carrito = cursor.lastrowid
        
    # Verificar si el producto ya existe en los ítems de este carrito
    cursor.execute("SELECT cantidad FROM carritoItems WHERE id_carrito = ? AND id_producto = ?", (id_carrito, id_producto))
    item_existente = cursor.fetchone()
    
    if item_existente:
        nueva_cantidad = item_existente['cantidad'] + cantidad_solicitada
        # Si la suma supera el stock real, topamos la cantidad al máximo disponible
        if nueva_cantidad > stock_disponible:
            nueva_cantidad = stock_disponible
            
        nuevo_subtotal = precio_unitario * nueva_cantidad
        cursor.execute(
            "UPDATE carritoItems SET cantidad = ?, subTotal = ? WHERE id_carrito = ? AND id_producto = ?",
            (nueva_cantidad, nuevo_subtotal, id_carrito, id_producto)
        )
    else:
        # Aseguramos que la cantidad inicial tampoco supere el stock
        if cantidad_solicitada > stock_disponible:
            cantidad_solicitada = stock_disponible
            
        if cantidad_solicitada > 0:
            subtotal = precio_unitario * cantidad_solicitada
            cursor.execute(
                "INSERT INTO carritoItems (id_carrito, id_producto, cantidad, subTotal) VALUES (?, ?, ?, ?)",
                (id_carrito, id_producto, cantidad_solicitada, subtotal)
            )
        
    db.commit()
    
    return redirect(url_for('carrito.ver_carrito'))

# Ruta para eliminar un producto específico del carrito
@carrito_bp.route('/carrito/eliminar/<int:id_producto>', methods=['POST'])
def eliminar_producto(id_producto):
    if not session.get('id_usuario'):
        return redirect(url_for('login'))
        
    id_usuario = session['id_usuario']
    db = get_db()
    cursor = db.cursor()
    
    # 1. Obtener el id_carrito del usuario actual
    cursor.execute("SELECT id_carrito FROM carritos WHERE id_usuario = ?", (id_usuario,))
    carrito = cursor.fetchone()
    
    if carrito:
        id_carrito = carrito['id_carrito']
        
        # 2. Eliminar el registro correspondiente en carritoItems
        cursor.execute(
            "DELETE FROM carritoItems WHERE id_carrito = ? AND id_producto = ?",
            (id_carrito, id_producto)
        )
        db.commit()
        
    # Recargar la vista del carrito
    return redirect(url_for('carrito.ver_carrito'))