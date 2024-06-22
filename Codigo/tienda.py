from orden import Orden, ItemOrden

class Tienda:
    def __init__(self):
        self.productos = []
        self.clientes = []
        self.ordenes = []
        self.categorias = []
    
    def registrar_producto(self, producto):
        self.productos.append(producto)
    
    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def crear_orden(self, cliente):
        orden = Orden(cliente)
        self.ordenes.append(orden)
        return orden
    
    def obtener_producto_por_nombre(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None  
    
    def mostrar_productos(self):
        return self.productos
    
    def mostrar_clientes(self):
        return self.clientes
    
    def mostrar_ordenes(self):
        return self.ordenes
    
    def mostrar_categorias(self):
        return self.categorias
