class Producto: 
    
    def __init__(self, nombre, precio, categoria, stock ):
        
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        
    def __str__(self):
        return f'Nombre del porducto: {self.nombre}\n Precio del producto: {self.precio}\n Categoria del producto: {self.categoria}'
    