from dao.libro_dao import LibroDAO
from models.libro import Libro

def ver_libros():
    try:
        libro_dao = LibroDAO()
        libros = libro_dao.obtener_todo()

        if len(libros) == 0:
            print("No hay libros registrado")
        else:
            for libro in libros:
                print (f" {libro.id} {libro.titulo} {libro.autor} {libro.isbn} {libro.disponible} ")
        print("\n Conexion esxitosa con la base de datos")

    except Exception as e:
        print("Existe un error")
        print(e)
    
def insertar_libro():
    print("INSERTAR UN NUVEO LIBRO")
    titulo = input("Escribe el titulo:")
    autor = int(input("Escribe el id del autor:"))
    isbn = input("Escribe el isbn")
    disponible = True
    
    try:
        libro_dao = LibroDAO()
        ultimo_id = libro_dao.obtener_ultimo_id() + 1
        libro = Libro(ultimo_id, titulo, autor, isbn, disponible)
        libro_dao.insertar(libro)
        print("Insercion del nuevo libro fue existosa")
    except Exception as e:
        print("Error al insertar el libro")
        print(e)

def actualizar_libro():
    try:
        libro_dao = LibroDAO()
        print("Lista de libros disponibles")
        libro_dao.obtener_todo()
        id = int(input("Seleccione el id del libro a actualizar"))
        titulo = input("Escribe el titulo:")
        autor = int(input("Escribe el id del autor:"))
        isbn = input("Escribe el isbn")
        disponible = bool(input("Escribe si esta disponible:"))
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.actualizar(libro)
        print("El libro fue actualizado con exito")
    except Exception as e:
        print("Error al actualizar el libro")
        print(e)

def eliminar_libro():
    try:
        libro_dao = LibroDAO()
        print("Lista de libro disponibles")
        libro_dao.obtener_todo()
        id = int(input("Escribe el id del libro a eliminar"))
        libro_dao.eliminar(id)
    except Exception as e:
        print(f"Error al aliminar el libro {id}")
        print(e)




def main():
    print("=== BIBLIOTECA UNIVERSITARIA ===")
    print("1. ver todos los libros")
    print("2. insertar un nuevo libro")
    print("3. Actualizar libro existente")
    print("4. Eliminar un libro existente")
    opcion = int(input("Selecciona una opcion (1-4):"))

    match opcion:
        case 1:
            ver_libros()
        case 2:
            insertar_libro()
        case 3:
            actualizar_libro()
        case 3:
            eliminar_libro()


if __name__ == "__main__":
    main()