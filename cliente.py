# cliente.py

class Cliente:
    def __init__(self, nombre, apellido, id_cliente):
        self.nombre = nombre
        self.apellido = apellido
        self.id_cliente = id_cliente
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, ID Cliente: {self.id_cliente}"
