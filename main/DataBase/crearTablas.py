import sqlite3

conexion = sqlite3.connect("main/DataBase/masusuDataBase.db")

cursor = conexion.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT UNIQUE NOT NULL,
    contrasena TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    producto TEXT NOT NULL,
    categoria TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL,   
    descripcion VARCHAR(375) NOT NULL,   
    imagen TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS carritos (
    id_carrito INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER UNIQUE NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS carritoItems (
    id_carrito INTEGER,
    id_producto INTEGER,
    cantidad INTEGER NOT NULL,
    subTotal REAL NOT NULL,
    PRIMARY KEY (id_carrito, id_producto),
    FOREIGN KEY (id_carrito) REFERENCES carritos(id_carrito) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ordenes (
    id_orden INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    montoTotal REAL NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS detalle_orden (
    id_orden INTEGER,
    id_producto INTEGER,
    cantidad INTEGER NOT NULL,
    precio_unitario REAL NOT NULL,
    subtotal REAL NOT NULL,
    FOREIGN KEY (id_orden) REFERENCES ordenes(id_orden) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);
""")


conexion.commit()