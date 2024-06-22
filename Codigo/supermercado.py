import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox, QTextEdit, QSpinBox
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

from producto import Producto, Categoria
from cliente import Cliente
from tienda import Tienda, Orden
from Factura import Factura

class SupermercadoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gestión de Tienda")
        self.setGeometry(100, 100, 800, 800) 
        
        self.tienda = Tienda()
        self.productos_en_orden = []
        self.factura = Factura()
        
        self.setup_ui()
        self.cargar_datos_iniciales()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        image_path = "C:/Users/LexV/Desktop/Python/Supermercado/Supermercado1/Gestor Supermercado/Logo.png"

        self.setStyleSheet(f"""
            QMainWindow {{
                background-image: url({image_path});
                background-repeat: no-repeat;
                background-position: center;
                background-attachment: fixed;
            }}
        """)

        layout_principal = QVBoxLayout()
        central_widget.setLayout(layout_principal)

        layout_principal.addWidget(self.crear_groupbox_productos())
        layout_principal.addWidget(self.crear_groupbox_clientes())
        layout_principal.addWidget(self.crear_groupbox_ordenes())
        layout_principal.addWidget(self.crear_factura_textedit())
        layout_principal.addWidget(self.crear_btn_salir())
    
    def crear_groupbox_productos(self):
        groupbox_productos = QWidget()
        layout_productos = QVBoxLayout()
        groupbox_productos.setLayout(layout_productos)
        
        layout_productos.addWidget(QLabel("Nombre del Producto:"))
        self.nombre_producto_input = QLineEdit()
        self.estilo_widget_personalizado(self.nombre_producto_input)
        layout_productos.addWidget(self.nombre_producto_input)
        
        layout_productos.addWidget(QLabel("Cantidad:"))
        self.cantidad_producto_input = QSpinBox()
        self.cantidad_producto_input.setFixedSize(50, 25)
        self.estilo_widget_personalizado(self.cantidad_producto_input)
        self.cantidad_producto_input.setMinimum(1)
        layout_productos.addWidget(self.cantidad_producto_input)
        
        layout_productos.addWidget(QLabel("Precio:"))
        self.precio_producto_input = QLineEdit()
        self.estilo_widget_personalizado(self.precio_producto_input)
        layout_productos.addWidget(self.precio_producto_input)
        
        layout_productos.addWidget(QLabel("Categoría:"))
        self.categoria_producto_input = QComboBox()
        self.estilo_widget_personalizado(self.categoria_producto_input)
        layout_productos.addWidget(self.categoria_producto_input)
        
        btn_registrar_producto = QPushButton("Registrar Producto")
        btn_registrar_producto.clicked.connect(self.registrar_producto)
        layout_productos.addWidget(btn_registrar_producto)
        
        return groupbox_productos
    
    def crear_groupbox_clientes(self):
        groupbox_clientes = QWidget()
        layout_clientes = QVBoxLayout()
        groupbox_clientes.setLayout(layout_clientes)
        
        layout_clientes.addWidget(QLabel("Nombre del Cliente:"))
        self.nombre_cliente_input = QLineEdit()
        self.estilo_widget_personalizado(self.nombre_cliente_input)
        layout_clientes.addWidget(self.nombre_cliente_input)
        
        layout_clientes.addWidget(QLabel("Apellido:"))
        self.apellido_cliente_input = QLineEdit()
        self.estilo_widget_personalizado(self.apellido_cliente_input)
        layout_clientes.addWidget(self.apellido_cliente_input)
        
        layout_clientes.addWidget(QLabel("ID Cliente:"))
        self.id_cliente_input = QLineEdit()
        self.estilo_widget_personalizado(self.id_cliente_input)
        layout_clientes.addWidget(self.id_cliente_input)
        
        btn_registrar_cliente = QPushButton("Registrar Cliente")
        btn_registrar_cliente.clicked.connect(self.registrar_cliente)
        layout_clientes.addWidget(btn_registrar_cliente)
        
        return groupbox_clientes
    
    def crear_groupbox_ordenes(self):
        groupbox_ordenes = QWidget()
        layout_ordenes = QVBoxLayout()
        groupbox_ordenes.setLayout(layout_ordenes)
        
        layout_ordenes.addWidget(QLabel("Seleccione un Cliente:"))
        self.cliente_combobox = QComboBox()
        self.estilo_widget_personalizado(self.cliente_combobox)
        layout_ordenes.addWidget(self.cliente_combobox)
        
        btn_agregar_producto = QPushButton("Agregar Producto")
        btn_agregar_producto.clicked.connect(self.agregar_producto)
        layout_ordenes.addWidget(btn_agregar_producto)
        
        btn_crear_orden = QPushButton("Crear Orden")
        btn_crear_orden.clicked.connect(self.crear_orden)
        layout_ordenes.addWidget(btn_crear_orden)
        
        return groupbox_ordenes
    
    def crear_factura_textedit(self):
        self.factura_textedit = QTextEdit()
        self.factura_textedit.setReadOnly(True)
        self.estilo_widget_personalizado(self.factura_textedit)
        return self.factura_textedit
    
    def crear_btn_salir(self):
        btn_salir = QPushButton("Salir")
        btn_salir.clicked.connect(self.salir)
        return btn_salir
    
    def salir(self):
        sys.exit()
    
    def cargar_datos_iniciales(self):
        categorias = ["Electrónica", "Ropa", "Alimentos"]
        self.categoria_producto_input.addItems(categorias)
        
        self.cliente_combobox.addItem("Seleccione un cliente...")
        for cliente in self.tienda.clientes:
            self.cliente_combobox.addItem(f"{cliente.nombre} {cliente.apellido}")
    
    def registrar_producto(self):
        nombre = self.nombre_producto_input.text()
        precio = float(self.precio_producto_input.text())
        categoria_nombre = self.categoria_producto_input.currentText()
        
        categoria = Categoria(categoria_nombre)
        producto = Producto(nombre, precio, categoria)
        self.tienda.registrar_producto(producto)
        
        QMessageBox.information(self, "Registro de Producto", f"Producto '{nombre}' registrado correctamente.")
    
    def registrar_cliente(self):
        nombre = self.nombre_cliente_input.text()
        apellido = self.apellido_cliente_input.text()
        id_cliente = int(self.id_cliente_input.text())
        
        cliente = Cliente(nombre, apellido, id_cliente)
        self.tienda.registrar_cliente(cliente)
        
        self.cliente_combobox.addItem(f"{nombre} {apellido}")
        QMessageBox.information(self, "Registro de Cliente", f"Cliente '{nombre} {apellido}' registrado correctamente.")
    
    def agregar_producto(self):
        nombre = self.nombre_producto_input.text()
        cantidad = self.cantidad_producto_input.value()
        
        producto = self.tienda.obtener_producto_por_nombre(nombre)
        if producto:
            for _ in range(cantidad):
                self.factura.agregar_producto(producto.nombre, producto.precio)
            self.actualizar_factura()
            QMessageBox.information(self, "Agregar Producto", f"{cantidad} productos '{nombre}' agregados a la factura.")
        else:
            QMessageBox.critical(self, "Error", f"Producto '{nombre}' no encontrado en la tienda.")
    
    def crear_orden(self):
        if self.cliente_combobox.currentIndex() <= 0:
            QMessageBox.critical(self, "Error", "Seleccione un cliente válido.")
            return
        
        cliente_index = self.cliente_combobox.currentIndex() - 1
        cliente_seleccionado = self.tienda.clientes[cliente_index]
        
        orden = Orden(cliente_seleccionado)
        
        for producto in self.productos_en_orden:
            orden.agregar_item(producto)
        
        self.actualizar_factura()
        QMessageBox.information(self, "Creación de Orden", "Orden creada correctamente.")
    
    def actualizar_factura(self):
        factura_generada = self.factura.generar_factura()
        self.factura_textedit.setPlainText(factura_generada)
    
    def estilo_widget_personalizado(self, widget):
        # Define el color personalizado
        color_personalizado = QColor("#DCDCDC")
        
        # Aplica el estilo al widget
        widget.setStyleSheet(f"""
            background-color: {color_personalizado.name()};
            color: black;
            border: 1px solid black;
            selection-background-color: #F5F5DC;  /* Color de fondo de selección */
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SupermercadoApp()
    window.show()
    sys.exit(app.exec_())
