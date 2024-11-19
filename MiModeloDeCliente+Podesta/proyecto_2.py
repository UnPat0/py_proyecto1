
class Cliente:
    
    def __init__(self, nombre, email, password, compras = []):
        
        total_clientes = 0
        
        if compras is None:
            compras = []
        self.nombre = nombre
        self.email = email
        self.password = password
        self.compras = compras
        total_clientes += 1
        
    def __str__(self):
        return f'Nombre: {self.nombre}, Email: {self.email}, Compras: {self.compras}'
        

class Producto: 
    
    def __init__(self, nombre, precio, categoria, stock ):
        
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        
    def __str__(self):
        return f'Nombre del porducto: {self.nombre}\n Precio del producto: {self.precio}\n Categoria del producto: {self.categoria}'
    
class Carrito:
    
    def __init__(self):
        self.carrito = []
        
    def agregar_producto(self, producto):
        
        if isinstance(producto, Producto):
            self.carrito.append(producto)
            return f'Producto {producto.nombre} agregado al carrito'
        else:
            return 'Error: debe agregar una instancia de Producto'
    
    def eliminar_producto(self, producto):
        if producto in self.carrito:
            self.carrito.remove(producto)
            return 'Producto eliminado correctamente'
        else:
            return 'Producto no encontrado en el carrito'
    
    def mostrar_carrito(self):
        
        if not self.carrito:
            return 'El carrito está vacío'
        
        print("Productos en el carrito:")
        for producto in self.carrito:
            print(producto)
        return ''
    
mi_carrito = Carrito()

producto1 = Producto("Manzana", 0.5, "Frutas", 50)
producto2 = Producto("Galletas de Chocolate", 1.00, "Comestibles", 300)


print(mi_carrito.agregar_producto(producto1))
print(mi_carrito.agregar_producto(producto2))


mi_carrito.mostrar_carrito()

        
        
        
