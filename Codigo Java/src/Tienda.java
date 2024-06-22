
package gestorsupermercado;

import java.util.ArrayList;
import java.util.List;

public class Tienda {
     private List<Producto> productos;
    private List<Cliente> clientes;

    public Tienda() {
        productos = new ArrayList<>();
        clientes = new ArrayList<>();
    }

    public void registrarProducto(Producto producto) {
        productos.add(producto);
    }

    public Producto obtenerProductoPorNombre(String nombre) {
        for (Producto producto : productos) {
            if (producto.getNombre().equals(nombre)) {
                return producto;
            }
        }
        return null;
    }

    public void registrarCliente(Cliente cliente) {
        clientes.add(cliente);
    }

    public List<Cliente> getClientes() {
        return clientes;
    }

    public List<Producto> getProductos() {
        return productos;
    }
}