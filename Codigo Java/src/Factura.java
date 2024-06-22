
package gestorsupermercado;


import java.util.ArrayList;
import java.util.List;

public class Factura {
     private List<String> productos;
    private double total;

    public Factura() {
        productos = new ArrayList<>();
        total = 0.0;
    }

    public void agregarProducto(String nombre, double precio) {
        productos.add(nombre + " - $" + precio);
        total += precio;
    }

    public String generarFactura() {
        StringBuilder sb = new StringBuilder();
        for (String producto : productos) {
            sb.append(producto).append("\n");
        }
        sb.append("Total: $").append(total);
        return sb.toString();
    }
}