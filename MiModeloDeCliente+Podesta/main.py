with open("C:\\Users\\pps38\\OneDrive\\Documentos\\los .py\\productos.csv", 'r') as lista_de_productos:
    
    contenido = lista_de_productos.read()
    

from mi_paquete import Cliente, Producto, Carrito
    

producto1 = Producto("Libro de Aventura", 10.00, "Ocio", 50)
producto2 = Producto("Galletas de Chocolate", 1.00, "Comestibles", 300)

cliente1 = Cliente("Juan", "juan@email.com", "juan123", [Producto == producto1])





