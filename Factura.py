class Factura:
    def __init__(self):
        self.productos = []  # Lista para almacenar los productos en la factura
        self.total = 0.0     # Inicializar el total en cero
    
    def agregar_producto(self, nombre, precio):
        self.productos.append((nombre, precio))  # Agregar el producto como una tupla (nombre, precio)
        self.total += precio                    # Sumar el precio al total
    
    def generar_factura(self):
        factura = f"FACTURA\n"
        
        for nombre, precio in self.productos:
            factura += f"- {nombre}: ${precio:.2f}\n"
        
        factura += f"\nTotal: ${self.total:.2f}"
        
        return factura
