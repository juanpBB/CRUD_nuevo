class Producto:
    def __init__(self, nombre, titulo, autor):
        self.nombre=nombre
        self.titulo=titulo
        self.autor=autor 
    def paraConexiondb(self):
        return{
            'nombre':self.nombre,
            'titulo':self.titulo,
            'autor':self.autor
            
        }
        