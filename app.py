from dao.libro_dao import LibroDAO

def main():
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

if __name__ == "__main__":
    main()