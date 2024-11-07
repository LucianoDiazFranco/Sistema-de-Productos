import sqlite3

# Crear una conexión a la base de datos (creará el archivo si no existe)
conexion = sqlite3.connect('gestion.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

###################CREACION DE TABLAS#########################

# Crear tabla Cliente
cursor.execute('''
    CREATE TABLE IF NOT EXISTS CLIENTES (
        DNI VARCHAR(10) PRIMARY KEY,
        Nombre VARCHAR(50)
    )
''')

# Crear tabla Producto
cursor.execute('''
    CREATE TABLE IF NOT EXISTS PRODUCTOS (
        Nombre VARCHAR(50),
        PRECIO INTEGER
    )
''')

# Crear tabla Distrito
cursor.execute('''
    CREATE TABLE IF NOT EXISTS DISTRITO (
        id_distrito INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(50) NOT NULL,
        origen VARCHAR(50),
        distancia REAL
    )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ORDEN (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto VARCHAR(50),
    cliente VARCHAR(10),
    distrito VARCHAR(50),
    FOREIGN KEY (producto) REFERENCES PRODUCTOS(Nombre),
    FOREIGN KEY (cliente) REFERENCES CLIENTES(DNI),
    FOREIGN KEY (distrito) REFERENCES Distrito(nombre)
)
''')


# Confirmar los cambios
conexion.commit()

# Cerrar la conexión
conexion.close()

print("Base de datos y tablas creadas exitosamente.")
