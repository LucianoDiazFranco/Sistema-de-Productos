import sqlite3

class Funciones:
    def __init__(self, db_name='gestion.db'):
        self.db_name = db_name

    def conectar_bd(self):
        # Conectar a la base de datos y devolver la conexión
        return sqlite3.connect(self.db_name)


#################################### LOGICA AGREGAR PRODUCTOS #########################################
    def agregar_producto(self, nombre, precio):
        # Conectar a la base de datos
        conexion = self.conectar_bd()
        cursor = conexion.cursor()
        
        # Verificar si el producto ya existe
        cursor.execute("SELECT COUNT(*) FROM PRODUCTOS WHERE Nombre = ?", (nombre,))
        if cursor.fetchone()[0] > 0:
            print("Producto ya existe en la base de datos.")
        else:
            # Insertar el producto en la base de datos
            cursor.execute("INSERT INTO PRODUCTOS (Nombre, PRECIO) VALUES (?, ?)", (nombre, precio))
            conexion.commit()
            print("Producto agregado exitosamente.")
            # Cerrar la conexión
        conexion.close()
####################################### Logica agregar Cliente ###########################################

    def agregar_cliente(self, dni, nombre):
        # Conectar a la base de datos
        conexion = self.conectar_bd()
        cursor = conexion.cursor()
        
        # Verificar si el cliente ya existe
        cursor.execute("SELECT COUNT(*) FROM CLIENTES WHERE DNI = ?", (dni,))
        if cursor.fetchone()[0] > 0:
            print("Cliente ya existe en la base de datos.")
        else:
            # Insertar el cliente en la base de datos
            cursor.execute("INSERT INTO CLIENTES (DNI, Nombre) VALUES (?, ?)", (dni, nombre))
            conexion.commit()
            print("Cliente agregado exitosamente.")
        
        # Cerrar la conexión
        conexion.close()

###########################################################################
    def agregar_distrito(self, nombre, coordenada_x, coordenada_y, distancia):
        # Conectar a la base de datos
        conexion = self.conectar_bd()
        cursor = conexion.cursor()
        
        # Verificar si el distrito ya existe
        cursor.execute("SELECT COUNT(*) FROM DISTRITO WHERE nombre = ?", (nombre,))
        if cursor.fetchone()[0] > 0:
            print("Distrito ya existe en la base de datos.")
        else:
            # Insertar el distrito en la base de datos
            cursor.execute(
                "INSERT INTO DISTRITO (nombre, coordenada_x, coordenada_y, distancia) VALUES (?, ?, ?, ?)",
                (nombre, coordenada_x, coordenada_y, distancia)
            )
            conexion.commit()
            print("Distrito agregado exitosamente.")
        
        # Cerrar la conexión
        conexion.close()
##########################################################################################
    def agregar_orden(self, producto_nombre, cliente_dni, distrito_nombre):
        conexion = self.conectar_bd()
        cursor = conexion.cursor()
        
        # Verificar que el producto exista
        cursor.execute("SELECT Nombre FROM PRODUCTOS WHERE Nombre = ?", (producto_nombre,))
        producto = cursor.fetchone()
        if not producto:
            print("Error: Producto no encontrado.")
            conexion.close()
            return

        # Verificar que el cliente exista
        cursor.execute("SELECT DNI FROM CLIENTES WHERE DNI = ?", (cliente_dni,))
        cliente = cursor.fetchone()
        if not cliente:
            print("Error: Cliente no encontrado.")
            conexion.close()
            return

        # Verificar que el distrito exista
        cursor.execute("SELECT nombre FROM DISTRITO WHERE nombre = ?", (distrito_nombre,))
        distrito = cursor.fetchone()
        if not distrito:
            print("Error: Distrito no encontrado.")
            conexion.close()
            return

        # Insertar la orden en la base de datos si todos los datos existen
        cursor.execute(
            "INSERT INTO ORDEN (producto, cliente, distrito) VALUES (?, ?, ?)",
            (producto_nombre, cliente_dni, distrito_nombre)
        )
        conexion.commit()
        print("Orden agregada exitosamente.")
##########################################################################################

    def listar_productos(self):
        conexion = self.conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT Nombre, PRECIO FROM PRODUCTOS")
        productos = cursor.fetchall()
        conexion.close()
        return productos

    def listar_clientes(self):
        conexion = self.conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT DNI, Nombre FROM CLIENTES")
        clientes = cursor.fetchall()
        conexion.close()
        return clientes

    def listar_distritos(self): 
        conexion = self.conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, distancia FROM DISTRITO")  # Consulta SQL corregida
        distritos = cursor.fetchall()
        conexion.close()
        return distritos

    def listar_ordenes(self):
        conexion = self.conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT producto, cliente, distrito FROM ORDEN")
        ordenes = cursor.fetchall()
        conexion.close()
        return ordenes
    
        # Cerrar la conexión
        conexion.close()