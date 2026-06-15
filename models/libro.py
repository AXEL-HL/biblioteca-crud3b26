class Libro:

    #Constructor
    def __init__(self, id , titulo, autor, isbn, disponible):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def prestar(self):
        self.disponible = False

    def devolver(self):
        self.disponible = True

    def mostrar_info(self):
        self.disponible = "Disponible" if self.disponible else "No disponible"
        return f"ID: {self.id}, Titulo: {self.titulo}, Autor: {self.autor.nombre}, ISBN: {self.isbn}, Estado: {self.disponible}"
    

        