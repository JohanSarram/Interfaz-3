
class ItemOrden:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
    
    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad

class Orden:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []
        self.total = 0
    
    def agregar_item(self, item):
        self.items.append(item)
        self.total += item.calcular_subtotal()
    
    def calcular_total(self):
        return self.total
