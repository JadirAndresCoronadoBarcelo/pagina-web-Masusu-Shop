from flask import Flask, render_template

app = Flask(__name__)

# Ruta para el menú principal (página de inicio)
@app.route('/')
@app.route('/menu')
def menu_principal():
    return render_template('MenuPrincipal.html')

# Ruta para el login de usuarios
@app.route('/login')
def login():
    return render_template('login.html')

# Ruta para el carrito de compras
@app.route('/carrito')
def carrito():
    return render_template('carrito.html')

# Ruta para la vista de detalle de un producto
@app.route('/producto')
def producto_vista():
    return render_template('productoVista.html')

# Rutas para cada una de tus categorías (según tus archivos HTML)
@app.route('/categoria/mouses')
def categoria_mouses():
    return render_template('categoriaMouses.html')

@app.route('/categoria/teclados')
def categoria_teclados():
    return render_template('categoriaTeclados.html')

@app.route('/categoria/diademas')
def categoria_diademas():
    return render_template('categoriaDiademas.html')

@app.route('/categoria/sillas')
def categoria_sillas():
    return render_template('categoriaSillas.html')

if __name__ == '__main__':
    app.run(debug=True)