
package gestorsupermercado;

import java.util.ArrayList;
import java.util.List;

public class Orden {
    private Cliente cliente;
    private List<Producto> items;

    public Orden(Cliente cliente) {
        this.cliente = cliente;
        this.items = new ArrayList<>();
    }

    public void agregarItem(Producto producto) {
        items.add(producto);
    }

    public Cliente getCliente() {
        return cliente;
    }

    public List<Producto> getItems() {
        return items;
    }
}