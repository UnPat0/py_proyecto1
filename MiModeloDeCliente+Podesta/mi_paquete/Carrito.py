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