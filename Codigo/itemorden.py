
class ItemOrden:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
    
    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad
