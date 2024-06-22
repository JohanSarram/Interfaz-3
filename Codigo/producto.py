
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar_info(self):
        return self.nombre

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Categoría: {self.categoria.mostrar_info()}"
