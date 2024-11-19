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
        return f'Nombre: {self.nombre}, Email: {self.email}'
        