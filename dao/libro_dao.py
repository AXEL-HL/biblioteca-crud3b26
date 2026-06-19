from database.conexion import Conexion
from models.libro import Libro

class LibroDAO:

#SELCT * from

    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM libro")
        registros = cursor.fetchall()

        libros = []
        for registros in registros:
            libro = Libro(
                id = registros[0],
                titulo= registros[1],
                autor = registros[2],
                isbn = registros[3],
                disponible= registros[4]
            )
            libros.append(libro)
        cursor.close()
        conexion.close()
        return libros 
    
    def insertar(self, libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO libro(id, titulo, autor, isbn, disponible)
        VALUES(%s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            libro.id,
            libro.titulo,
            libro.autor,
            libro.isbn,
            libro.disponible
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

        #UPDATE
    def actualizar(self, libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE libro
        SET titulo = %s, autor = %s, isbn = %s, disponible = %s
        WHERE id = %s
        """
        
        cursor.execute(sql, (
                        libro.titulo,
                        libro.autor,
                        libro.isbn,
                        libro.disponible,
                        libro.id
                        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # DELATE
    def eliminar(self,id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.escute("DELETE FROM libro WHERE id = %s", (id))

        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT MAX(id) FROM libro")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado[0] is None:
            return 0
        return resultado[0]

