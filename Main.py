import customtkinter as ctk
from tkinter import messagebox
from funciones import Funciones


# Configuración de CustomTkinter
ctk.set_appearance_mode("Dark")  # Modo oscuro
ctk.set_default_color_theme("blue")  # Tema de color

class GestionApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Sistema de Gestión de Ventas")
        self.geometry("800x600")
        
        self.sistema = Funciones()  # Instancia de Funciones para usar sus métodos de base de datos

        # Título
        self.title_label = ctk.CTkLabel(self, text="Sistema de Gestión de Ventas", font=("Arial", 24))
        self.title_label.pack(pady=20)

        # Frame para productos
        product_frame = ctk.CTkFrame(self)
        product_frame.pack(pady=10, padx=10, fill="x")
        
        self.add_product_button = ctk.CTkButton(product_frame, text="Agregar Producto", command=self.agregar_producto_menu)
        self.add_product_button.pack(side="left", padx=5)
        
        self.list_product_button = ctk.CTkButton(product_frame, text="Listar Productos", command=self.listar_productos)
        self.list_product_button.pack(side="left", padx=5)

        # Frame para clientes
        client_frame = ctk.CTkFrame(self)
        client_frame.pack(pady=10, padx=10, fill="x")
        
        self.add_client_button = ctk.CTkButton(client_frame, text="Agregar Cliente", command=self.agregar_cliente_menu)
        self.add_client_button.pack(side="left", padx=5)
        
        self.list_client_button = ctk.CTkButton(client_frame, text="Listar Clientes", command=self.listar_clientes)
        self.list_client_button.pack(side="left", padx=5)

        # Frame para distritos
        district_frame = ctk.CTkFrame(self)
        district_frame.pack(pady=10, padx=10, fill="x")

        self.add_district_button = ctk.CTkButton(district_frame, text="Agregar Distrito", command=self.agregar_distrito_menu)
        self.add_district_button.pack(side="left", padx=5)

        self.list_district_button = ctk.CTkButton(district_frame, text="Listar Distritos", command=self.listar_distritos)
        self.list_district_button.pack(side="left", padx=5)

        # Frame para órdenes
        order_frame = ctk.CTkFrame(self)
        order_frame.pack(pady=10, padx=10, fill="x")
        
        self.add_order_button = ctk.CTkButton(order_frame, text="Agregar Orden", command=self.agregar_orden_menu)
        self.add_order_button.pack(side="left", padx=5)
        
        self.list_order_button = ctk.CTkButton(order_frame, text="Listar Órdenes", command=self.listar_ordenes)
        self.list_order_button.pack(side="left", padx=5)

    # Métodos para listar datos
    def listar_productos(self):
        productos = self.sistema.listar_productos()
        if productos:
            product_list = "\n".join([f"{nombre} - ${precio}" for nombre, precio in productos])
            messagebox.showinfo("Productos", product_list)
        else:
            messagebox.showinfo("Productos", "No hay productos registrados.")

    def listar_clientes(self):
        clientes = self.sistema.listar_clientes()
        if clientes:
            client_list = "\n".join([f"{dni} - {nombre}" for dni, nombre in clientes])
            messagebox.showinfo("Clientes", client_list)
        else:
            messagebox.showinfo("Clientes", "No hay clientes registrados.")

    def listar_distritos(self):
        distritos = self.sistema.listar_distritos()
        if distritos:
            district_list = "\n".join([f"{nombre} - Distancia: {distancia}" for nombre, distancia in distritos])
            messagebox.showinfo("Distritos", district_list)
        else:
            messagebox.showinfo("Distritos", "No hay distritos registrados.")

    def listar_ordenes(self):
        ordenes = self.sistema.listar_ordenes()
        if ordenes:
            order_list = "\n".join([f"Producto: {producto}, Cliente: {cliente}, Distrito: {distrito}" for producto, cliente, distrito in ordenes])
            messagebox.showinfo("Órdenes", order_list)
        else:
            messagebox.showinfo("Órdenes", "No hay órdenes registradas.")

    def agregar_producto_menu(self):
        product_window = ctk.CTkToplevel(self)
        product_window.title("Agregar Producto")

        ctk.CTkLabel(product_window, text="Nombre del Producto:").pack(pady=5)
        product_name_entry = ctk.CTkEntry(product_window)
        product_name_entry.pack(pady=5)

        ctk.CTkLabel(product_window, text="Precio del Producto:").pack(pady=5)
        product_price_entry = ctk.CTkEntry(product_window)
        product_price_entry.pack(pady=5)

        def agregar_producto():
            nombre = product_name_entry.get()
            try:
                precio = float(product_price_entry.get())
                self.sistema.agregar_producto(nombre, precio)
                messagebox.showinfo("Éxito", f"Producto {nombre} agregado.")
                product_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "El precio debe ser un número.")

        ctk.CTkButton(product_window, text="Agregar", command=agregar_producto).pack(pady=10)

    def agregar_cliente_menu(self):
        client_window = ctk.CTkToplevel(self)
        client_window.title("Agregar Cliente")

        ctk.CTkLabel(client_window, text="DNI del Cliente:").pack(pady=5)
        client_dni_entry = ctk.CTkEntry(client_window)
        client_dni_entry.pack(pady=5)

        ctk.CTkLabel(client_window, text="Nombre del Cliente:").pack(pady=5)
        client_name_entry = ctk.CTkEntry(client_window)
        client_name_entry.pack(pady=5)

        def agregar_cliente():
            dni = client_dni_entry.get()
            nombre = client_name_entry.get()
            self.sistema.agregar_cliente(dni, nombre)
            messagebox.showinfo("Éxito", f"Cliente {nombre} agregado.")
            client_window.destroy()

        ctk.CTkButton(client_window, text="Agregar", command=agregar_cliente).pack(pady=10)

    def agregar_distrito_menu(self):
        district_window = ctk.CTkToplevel(self)
        district_window.title("Agregar Distrito")

        ctk.CTkLabel(district_window, text="Nombre del Distrito:").pack(pady=5)
        district_name_entry = ctk.CTkEntry(district_window)
        district_name_entry.pack(pady=5)

        ctk.CTkLabel(district_window, text="Coordenada X:").pack(pady=5)
        coord_x_entry = ctk.CTkEntry(district_window)
        coord_x_entry.pack(pady=5)

        ctk.CTkLabel(district_window, text="Coordenada Y:").pack(pady=5)
        coord_y_entry = ctk.CTkEntry(district_window)
        coord_y_entry.pack(pady=5)

        ctk.CTkLabel(district_window, text="Distancia:").pack(pady=5)
        distancia_entry = ctk.CTkEntry(district_window)
        distancia_entry.pack(pady=5)

        def agregar_distrito():
            nombre = district_name_entry.get()
            try:
                coord_x = float(coord_x_entry.get())
                coord_y = float(coord_y_entry.get())
                distancia = float(distancia_entry.get())
                self.sistema.agregar_distrito(nombre, coord_x, coord_y, distancia)
                messagebox.showinfo("Éxito", f"Distrito {nombre} agregado.")
                district_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Las coordenadas y la distancia deben ser números.")

        ctk.CTkButton(district_window, text="Agregar", command=agregar_distrito).pack(pady=10)

    def agregar_orden_menu(self):
        order_window = ctk.CTkToplevel(self)
        order_window.title("Agregar Orden")

        ctk.CTkLabel(order_window, text="Nombre del Producto:").pack(pady=5)
        product_entry = ctk.CTkEntry(order_window)
        product_entry.pack(pady=5)

        ctk.CTkLabel(order_window, text="DNI del Cliente:").pack(pady=5)
        client_entry = ctk.CTkEntry(order_window)
        client_entry.pack(pady=5)

        ctk.CTkLabel(order_window, text="Nombre del Distrito:").pack(pady=5)
        district_entry = ctk.CTkEntry(order_window)
        district_entry.pack(pady=5)

        def agregar_orden():
            producto = product_entry.get()
            cliente = client_entry.get()
            distrito = district_entry.get()
            self.sistema.agregar_orden(producto, cliente, distrito)
            messagebox.showinfo("Éxito", "Orden agregada.")
            order_window.destroy()

        ctk.CTkButton(order_window, text="Agregar", command=agregar_orden).pack(pady=10)

if __name__ == "__main__":
    app = GestionApp()
    app.mainloop()
