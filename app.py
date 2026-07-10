#==========================================================================================
#==========================================================================================

#Libro
import flet as ft

from ui.main_window import main_window
from dao.libro_dao import LibroDAO
from models.libro import Libro
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario



def ver_libros():
    try:
        libro_dao = LibroDAO()
        libros = libro_dao.obtener_todo()

        if len(libros) == 0:
            print("No hay libros registrado")
        else:
            for libro in libros:
                print (f"| {libro.id} | {libro.titulo} | {libro.autor} | {libro.isbn} | {libro.disponible} |")
        print("\n Conexion esxitosa con la base de datos")

    except Exception as e:
        print("Existe un error")
        print(e)

#==========================================================================================
    
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

#==========================================================================================

def actualizar_libro():
    try:
        libro_dao = LibroDAO()
        print("Lista de libros disponibles")
        ver_libros()
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

#==========================================================================================

def eliminar_libro():
    try:
        libro_dao = LibroDAO()
        print("Lista de libro disponibles")
        ver_libros()
        id = int(input("Escribe el id del libro a eliminar:"))
        libro_dao.eliminar(id)
        print(f"El libro {id} ha sido eliminado con exito")
    except Exception as e:
        print(f"Error al aliminar el libro {id}")
        print(e)


#==========================================================================================
#==========================================================================================

#Usuarios

def ver_usuarios():
    try:
        usuario_dao = UsuarioDAO()
        usuarios = usuario_dao.obtener_todo()

        if len(usuarios) == 0:
            print("No hay usuarios registrados")
        else:
            for usuario in usuarios:
                print (f"| {usuario.id} | {usuario.nombre} | {usuario.matricula} | {usuario.carrera} | {usuario.correo} | {usuario.activo} ")
        print("\n Conexion esxitosa con la base de datos")

    except Exception as e:
        print("Existe un error")
        print(e)

#==========================================================================================
    
def insertar_usuario():
    print("INSERTAR UN NUVEO Usuario")
    nombre = input("Escribe el nombre del usuario:")
    matricula = int(input("Escribe la matricula del usuario:"))
    carrera = input("Escribe la carrera:")
    correo = input("Escribe el correo:")
    activo = True
    
    try:
        usuario_dao = UsuarioDAO()
        ultimo_id = usuario_dao.obtener_ultimo_id() + 1
        usuario = Usuario(ultimo_id, nombre, matricula, carrera, correo, activo)
        usuario_dao.insertar(usuario)
        print("Insercion del nuevo usuario fue existosa")
    except Exception as e:
        print("Error al insertar el usuario")
        print(e)

#==========================================================================================

def actualizar_usuario():
    try:

        usuario_dao = UsuarioDAO()
        print("Lista de usuarios disponibles")
        ver_usuarios()
        id = int(input("Seleccione el id del libro a actualizar"))
        nombre = input("Escribe el nombre:")
        matricula = input("Escribe la matricula")
        carrera = int(input("Escribe la carrera:"))
        correo = input("Escribe el correo:")
        activo = bool(input("Escribe si esta activo:"))
        usuario = Usuario(id, nombre, matricula, carrera, correo, activo)
        usuario_dao.actualizar(usuario)
        print("El usuario fue actualizado con exito")
    except Exception as e:
        print("Error al actualizar el usuario")
        print(e)

    #==========================================================================================

def eliminar_usuario():
    try:
        usuario_dao = UsuarioDAO()
        print("Lista de usuarios disponibles")
        ver_usuarios()
        id = int(input("Escribe el id del usuario a eliminar:"))
        usuario_dao.eliminar(id)
        print(f"El usuario {id} ha sido eliminado con exito")
    except Exception as e:
        print(f"Error al aliminar el usuario {id}")
        print(e)

#==========================================================================================

def menu_libros():
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
        case 4:
            eliminar_libro()

#==========================================================================================

def menu_usuarios():
    print("1. ver todos los usuarios")
    print("2. insertar un nuevo usuarios")
    print("3. Actualizar usuarios existente")
    print("4. Eliminar un usuarios existente")
    opcion = int(input("Selecciona una opcion (1-4):"))

    match opcion:
        case 1:
            ver_usuarios()
        case 2:
            insertar_usuario()
        case 3:
            actualizar_usuario()
        case 4:
            eliminar_usuario()

#==========================================================================================

ft.app(target=main_window)
# def main():
#     print("=== BIBLIOTECA UNIVERSITARIA ===")
#     print("Menu de opciones:")
#     print("1. Libros")
#     print("2. Usuarios")
#     opcion = int(input("Escribe tu opcion: "))
#     match opcion:
#         case 1: menu_libros()
#         case 2: menu_usuarios()

#     print("Saliendo del sistema de Biblioteca universitaria....")


# if __name__ == "__main__":
#  main()
