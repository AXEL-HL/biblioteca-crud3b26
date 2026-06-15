class Usuario:

    #constructor
    def __init__(self, id, nombre, matricula, carrera, correo, activo):
        self.id = id
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.correo = correo
        self.activo = activo

        def activar(self):
            self.activo = True
        
        def desactivar(self):
            self.activo = False

        def mostrar_info(self):
            return f"ID: {self.id}, Nombre:{self.nombre}, Matricula: {self.matricula}, Carrera: {self.carrera.nombre_carrera}, correo: {self.correo}, Activo: {self.activo}"
        