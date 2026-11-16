from flask import Blueprint, request, redirect, url_for, session, g
import sqlite3

# Creamos el Blueprint
auth_bp = Blueprint('auth', __name__)
DATABASE = 'masusuDatabase.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@auth_bp.teardown_request
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Ruta que procesa el Registro (POST)
@auth_bp.route('/registro', methods=['POST'])
def registro_post():
    nombre = request.form['nombre']
    correo = request.form['correo']
    contrasena = request.form['contrasena']
    
    db = get_db()
    cursor = db.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO usuarios (nombre, correo, contrasena) VALUES (?, ?, ?)",
            (nombre, correo, contrasena)
        )
        db.commit()
        
        cursor.execute("SELECT id_usuario, nombre FROM usuarios WHERE correo = ?", (correo,))
        usuario = cursor.fetchone()
        
        session['id_usuario'] = usuario['id_usuario']
        session['nombre_usuario'] = usuario['nombre']
        
        return redirect(url_for('menu_principal'))
        
    except sqlite3.IntegrityError:
        return "El correo electrónico ya se encuentra registrado. <a href='/login'>Volver</a>"

# Ruta que procesa el Inicio de Sesión (POST)
@auth_bp.route('/iniciar_sesion', methods=['POST'])
def login_post():
    correo = request.form['correo']
    contrasena = request.form['contrasena']
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE correo = ? AND contrasena = ?", (correo, contrasena))
    usuario = cursor.fetchone()
    
    if usuario:
        session['id_usuario'] = usuario['id_usuario']
        session['nombre_usuario'] = usuario['nombre']
        return redirect(url_for('menu_principal'))
    else:
        return "Correo o contraseña incorrectos. <a href='/login'>Intentar de nuevo</a>"

# Ruta para cerrar sesión
@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('menu_principal'))