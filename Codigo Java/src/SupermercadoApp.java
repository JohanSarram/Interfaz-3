package gestorsupermercado;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SupermercadoApp extends JFrame {
    private Tienda tienda;
    private Factura factura;
    private JTextArea facturaTextArea;
    private JTextField nombreProductoField;
    private JTextField precioProductoField;
    private JComboBox<String> categoriaProductoComboBox;
    private JTextField nombreClienteField;
    private JTextField apellidoClienteField;
    private JTextField idClienteField;
    private JComboBox<String> clienteComboBox;
    private JSpinner cantidadSpinner;

    public SupermercadoApp() {
        tienda = new Tienda();
        factura = new Factura();

        setTitle("Sistema de Gestión de Tienda");
        setSize(900, 700); // Tamaño ajustado
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        ImageIcon imageIcon = new ImageIcon(getClass().getClassLoader().getResource("gestorsupermercado/Logo.png"));
        JLabel background = new JLabel(imageIcon);
        setContentPane(background);
        setLayout(new BorderLayout());

        JPanel mainPanel = new JPanel();
        mainPanel.setOpaque(false); 
        mainPanel.setLayout(new GridBagLayout()); 
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(10, 10, 10, 10); 
        background.setLayout(new BorderLayout());
        background.add(mainPanel, BorderLayout.CENTER);

        gbc.gridx = 0;
        gbc.gridy = 0;
        mainPanel.add(crearPanelProductos(), gbc);

        gbc.gridx = 1;
        gbc.gridy = 0;
        mainPanel.add(crearPanelClientes(), gbc);

        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.gridwidth = 2; 
        mainPanel.add(crearPanelOrdenes(), gbc);

        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.gridwidth = 2; 
        mainPanel.add(crearPanelFactura(), gbc);

        cargarDatosIniciales();
    }

    private JPanel crearPanelProductos() {
    JPanel panel = new JPanel();
    panel.setOpaque(true); 
    panel.setBackground(new Color(255, 255, 255, 200)); 
    panel.setBorder(BorderFactory.createTitledBorder("Productos"));
    panel.setLayout(new GridLayout(5, 2, 10, 10));

    panel.add(new JLabel("Nombre del Producto:"));
    nombreProductoField = new JTextField();
    panel.add(nombreProductoField);

    panel.add(new JLabel("Cantidad:"));
    cantidadSpinner = new JSpinner(new SpinnerNumberModel(1, 1, 100, 1));
    panel.add(cantidadSpinner);

    panel.add(new JLabel("Precio:"));
    precioProductoField = new JTextField();
    panel.add(precioProductoField);

    panel.add(new JLabel("Categoría:"));
    categoriaProductoComboBox = new JComboBox<>();
    panel.add(categoriaProductoComboBox);

    JButton registrarProductoButton = new JButton("Registrar Producto");
    registrarProductoButton.addActionListener(new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
            registrarProducto();
        }
    });
    panel.add(registrarProductoButton);

    return panel;
}

private JPanel crearPanelClientes() {
    JPanel panel = new JPanel();
    panel.setOpaque(true);
    panel.setBackground(new Color(255, 255, 255, 200)); 
    panel.setBorder(BorderFactory.createTitledBorder("Clientes"));
    panel.setLayout(new GridLayout(4, 2, 10, 10));

    panel.add(new JLabel("Nombre del Cliente:"));
    nombreClienteField = new JTextField();
    panel.add(nombreClienteField);

    panel.add(new JLabel("Apellido:"));
    apellidoClienteField = new JTextField();
    panel.add(apellidoClienteField);

    panel.add(new JLabel("ID Cliente:"));
    idClienteField = new JTextField();
    panel.add(idClienteField);

    JButton registrarClienteButton = new JButton("Registrar Cliente");
    registrarClienteButton.addActionListener(new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
            registrarCliente();
        }
    });
    panel.add(registrarClienteButton);

    return panel;
}

private JPanel crearPanelOrdenes() {
    JPanel panel = new JPanel();
    panel.setOpaque(true);
    panel.setBackground(new Color(255, 255, 255, 200)); 
    panel.setBorder(BorderFactory.createTitledBorder("Órdenes"));
    panel.setLayout(new GridLayout(3, 2, 10, 10));

    panel.add(new JLabel("Seleccione un Cliente:"));
    clienteComboBox = new JComboBox<>();
    panel.add(clienteComboBox);

    JButton agregarProductoButton = new JButton("Agregar Producto");
    agregarProductoButton.addActionListener((ActionEvent e) -> {
        agregarProducto();
    });
    panel.add(agregarProductoButton);

    JButton crearOrdenButton = new JButton("Crear Orden");
    crearOrdenButton.addActionListener((ActionEvent e) -> {
        crearOrden();
    });
    panel.add(crearOrdenButton);

    return panel;
}

private JPanel crearPanelFactura() {
    JPanel panel = new JPanel();
    panel.setOpaque(true);
    panel.setBackground(new Color(255, 255, 255, 200)); 
    panel.setBorder(BorderFactory.createTitledBorder("Factura"));
    panel.setLayout(new BorderLayout());

    facturaTextArea = new JTextArea(10, 30);
    facturaTextArea.setEditable(false);
    panel.add(new JScrollPane(facturaTextArea), BorderLayout.CENTER);

    return panel;
}
    private void cargarDatosIniciales() {
        String[] categorias = {"Electrónica", "Ropa", "Alimentos"};
        for (String categoria : categorias) {
            categoriaProductoComboBox.addItem(categoria);
        }

        clienteComboBox.addItem("Seleccione un cliente...");
    }

    private void registrarProducto() {
        String nombre = nombreProductoField.getText();
        double precio = Double.parseDouble(precioProductoField.getText());
        String categoriaNombre = (String) categoriaProductoComboBox.getSelectedItem();

        Categoria categoria = new Categoria(categoriaNombre);
        Producto producto = new Producto(nombre, precio, categoria);
        tienda.registrarProducto(producto);

        JOptionPane.showMessageDialog(this, "Producto '" + nombre + "' registrado correctamente.");
    }

    private void registrarCliente() {
        String nombre = nombreClienteField.getText();
        String apellido = apellidoClienteField.getText();
        int idCliente = Integer.parseInt(idClienteField.getText());

        Cliente cliente = new Cliente(nombre, apellido, idCliente);
        tienda.registrarCliente(cliente);

        clienteComboBox.addItem(nombre + " " + apellido);
        JOptionPane.showMessageDialog(this, "Cliente '" + nombre + " " + apellido + "' registrado correctamente.");
    }

    private void agregarProducto() {
        String nombre = nombreProductoField.getText();
        int cantidad = (int) cantidadSpinner.getValue();

        Producto producto = tienda.obtenerProductoPorNombre(nombre);
        if (producto != null) {
            for (int i = 0; i < cantidad; i++) {
                factura.agregarProducto(producto.getNombre(), producto.getPrecio());
            }
            actualizarFactura();
            JOptionPane.showMessageDialog(this, cantidad + " productos '" + nombre + "' agregados a la factura.");
        } else {
            JOptionPane.showMessageDialog(this, "Producto '" + nombre + "' no encontrado en la tienda.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void crearOrden() {
        if (clienteComboBox.getSelectedIndex() <= 0) {
            JOptionPane.showMessageDialog(this, "Seleccione un cliente válido.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        int clienteIndex = clienteComboBox.getSelectedIndex() - 1;
        Cliente clienteSeleccionado = tienda.getClientes().get(clienteIndex);

        Orden orden = new Orden(clienteSeleccionado);

        for (Producto producto : tienda.getProductos()) {
            orden.agregarItem(producto);
        }

        actualizarFactura();
        JOptionPane.showMessageDialog(this, "Orden creada correctamente.");
    }

    private void actualizarFactura() {
        String facturaGenerada = factura.generarFactura();
        facturaTextArea.setText(facturaGenerada);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                SupermercadoApp app = new SupermercadoApp();
                app.setVisible(true);
            }
        });
    }
}
