class Factura:
    def __init__(self):
        self.productos = []  
        self.total = 0.0     
    
    def agregar_producto(self, nombre, precio):
        self.productos.append((nombre, precio))  
        self.total += precio                    
    
    def generar_factura(self):
        factura = f"FACTURA\n"
        
        for nombre, precio in self.productos:
            factura += f"- {nombre}: ${precio:.2f}\n"
        
        factura += f"\nTotal: ${self.total:.2f}"
        
        return factura
