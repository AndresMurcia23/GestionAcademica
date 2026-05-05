
def registrar_usuario(usuarios):
    print("\n===== CREAR USUARIO =====")

    nickname = input("Cree su nickname: ")
    contrasena = input("Cree su contraseña: ")

    for usuario in usuarios:
        if usuario["nickname"] == nickname:
            print("Error: Ese nickname ya existe.")
            return

    print("\nSeleccione su rol:")
    print("1. Estudiante")
    print("2. Profesor")

    opcion_rol = input("Digite una opción: ")

    match opcion_rol:
        case "1":
            rol = "ESTUDIANTE"
        case "2":
            rol = "PROFESOR"
        case _:
            print("Opción no válida. Se asignará rol ESTUDIANTE.")
            rol = "ESTUDIANTE"

    nuevo_usuario = {
        "nickname": nickname,
        "contrasena": contrasena,
        "rol": rol
    }

    usuarios.append(nuevo_usuario)

    print("\nUsuario creado correctamente.")
    print(f"Rol asignado: {rol}")


def login(usuarios):
    print("\n===== LOGIN =====")

    nickname = input("Digite su nickname: ")
    contrasena = input("Digite su contraseña: ")

    for usuario in usuarios:
        if usuario["nickname"] == nickname and usuario["contrasena"] == contrasena:
            print("\nInicio de sesión exitoso.")
            print(f"Bienvenido {usuario['nickname']}")
            print(f"Rol: {usuario['rol']}")
            return usuario

    print("\nUsuario o contraseña incorrectos.")
    return None


def crear_estudiante(estudiantes):
    print("\n===== CREAR ESTUDIANTE =====")

    id_estudiante = len(estudiantes) + 1
    nombre = input("Nombre: ")
    documento = input("Documento: ")
    correo = input("Correo: ")
    semestre = input("Semestre: ")

    estudiante = {
        "id": id_estudiante,
        "nombre": nombre,
        "documento": documento,
        "correo": correo,
        "semestre": semestre
    }

    estudiantes.append(estudiante)
    print("\nEstudiante creado correctamente.")


def listar_estudiantes(estudiantes):
    print("\n===== LISTA DE ESTUDIANTES =====")

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    for estudiante in estudiantes:
        print(f"ID: {estudiante['id']}")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Documento: {estudiante['documento']}")
        print(f"Correo: {estudiante['correo']}")
        print(f"Semestre: {estudiante['semestre']}")
        print("-----------------------------")


def crear_curso(cursos):
    print("\n===== CREAR CURSO =====")

    id_curso = len(cursos) + 1
    nombre = input("Nombre del curso: ")
    profesor = input("Profesor: ")

    try:
        cupos = int(input("Cupos: "))
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return

    curso = {
        "id": id_curso,
        "nombre": nombre,
        "profesor": profesor,
        "cupos": cupos
    }

    cursos.append(curso)
    print("\nCurso creado correctamente.")


def listar_cursos(cursos):
    print("\n===== LISTA DE CURSOS =====")

    if len(cursos) == 0:
        print("No hay cursos registrados.")
        return

    for curso in cursos:
        print(f"ID: {curso['id']}")
        print(f"Nombre: {curso['nombre']}")
        print(f"Profesor: {curso['profesor']}")
        print(f"Cupos disponibles: {curso['cupos']}")
        print("-----------------------------")


def inscribir_estudiante(estudiantes, cursos, inscripciones):
    print("\n===== INSCRIBIR ESTUDIANTE =====")

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    if len(cursos) == 0:
        print("No hay cursos registrados.")
        return

    listar_estudiantes(estudiantes)

    try:
        id_estudiante = int(input("Ingrese el ID del estudiante: "))
    except ValueError:
        print("Error: Debe ingresar un número.")
        return

    listar_cursos(cursos)

    try:
        id_curso = int(input("Ingrese el ID del curso: "))
    except ValueError:
        print("Error: Debe ingresar un número.")
        return

    estudiante_existe = False
    curso_encontrado = None

    for estudiante in estudiantes:
        if estudiante["id"] == id_estudiante:
            estudiante_existe = True

    for curso in cursos:
        if curso["id"] == id_curso:
            curso_encontrado = curso

    if not estudiante_existe:
        print("Error: El estudiante no existe.")
        return

    if curso_encontrado is None:
        print("Error: El curso no existe.")
        return

    if curso_encontrado["cupos"] <= 0:
        print("Error: No hay cupos disponibles.")
        return

    for inscripcion in inscripciones:
        if inscripcion["id_estudiante"] == id_estudiante and inscripcion["id_curso"] == id_curso:
            print("Error: El estudiante ya está inscrito en este curso.")
            return

    nueva_inscripcion = {
        "id_estudiante": id_estudiante,
        "id_curso": id_curso
    }

    inscripciones.append(nueva_inscripcion)
    curso_encontrado["cupos"] -= 1

    print("\nEstudiante inscrito correctamente.")


def registrar_nota(inscripciones, notas):
    print("\n===== REGISTRAR NOTA =====")

    if len(inscripciones) == 0:
        print("No hay estudiantes inscritos.")
        return

    try:
        id_estudiante = int(input("Ingrese el ID del estudiante: "))
        id_curso = int(input("Ingrese el ID del curso: "))
    except ValueError:
        print("Error: Debe ingresar números válidos.")
        return

    esta_inscrito = False

    for inscripcion in inscripciones:
        if inscripcion["id_estudiante"] == id_estudiante and inscripcion["id_curso"] == id_curso:
            esta_inscrito = True

    if not esta_inscrito:
        print("Error: El estudiante no está inscrito en ese curso.")
        return

    try:
        nota = float(input("Ingrese la nota de 0.0 a 5.0: "))
    except ValueError:
        print("Error: Debe ingresar un valor numérico.")
        return

    if nota < 0.0 or nota > 5.0:
        print("Error: La nota debe estar entre 0.0 y 5.0.")
        return

    nueva_nota = {
        "id_estudiante": id_estudiante,
        "id_curso": id_curso,
        "nota": nota
    }

    notas.append(nueva_nota)
    print("\nNota registrada correctamente.")


def ver_mis_notas(notas):
    print("\n===== MIS NOTAS =====")

    if len(notas) == 0:
        print("No hay notas registradas.")
        return

    for nota in notas:
        estado = "Aprobado" if nota["nota"] >= 3.0 else "Reprobado"
        print(f"Estudiante ID: {nota['id_estudiante']}")
        print(f"Curso ID: {nota['id_curso']}")
        print(f"Nota: {nota['nota']}")
        print(f"Estado: {estado}")
        print("-----------------------------")


def ver_mis_inscripciones(inscripciones):
    print("\n===== MIS INSCRIPCIONES =====")

    if len(inscripciones) == 0:
        print("No hay inscripciones registradas.")
        return

    for inscripcion in inscripciones:
        print(f"Estudiante ID: {inscripcion['id_estudiante']}")
        print(f"Curso ID: {inscripcion['id_curso']}")
        print("-----------------------------")


def estado_academico(notas):
    print("\n===== ESTADO ACADÉMICO =====")

    if len(notas) == 0:
        print("No hay notas registradas.")
        return

    for nota in notas:
        estado = "Aprobado" if nota["nota"] >= 3.0 else "Reprobado"
        print(f"Curso ID: {nota['id_curso']} - Nota: {nota['nota']} - {estado}")


def resumen_academico(estudiantes, cursos, inscripciones, notas):
    print("\n===== RESUMEN ACADÉMICO =====")

    print(f"Total de estudiantes: {len(estudiantes)}")
    print(f"Total de cursos: {len(cursos)}")
    print(f"Total de inscripciones: {len(inscripciones)}")
    print(f"Total de notas registradas: {len(notas)}")

    if len(notas) == 0:
        print("No hay notas para calcular.")
        return

    aprobados = 0
    reprobados = 0
    suma_notas = 0

    for nota in notas:
        suma_notas += nota["nota"]

        if nota["nota"] >= 3.0:
            aprobados += 1
        else:
            reprobados += 1

    promedio = suma_notas / len(notas)

    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")
    print(f"Promedio general: {promedio:.2f}")


def menu_profesor(estudiantes, cursos, inscripciones, notas):
    while True:
        print("\n===== MENÚ PROFESOR =====")
        print("1. Crear estudiante")
        print("2. Listar estudiantes")
        print("3. Crear curso")
        print("4. Listar cursos")
        print("5. Inscribir estudiante")
        print("6. Registrar nota")
        print("7. Ver resumen académico")
        print("8. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                crear_estudiante(estudiantes)
            case "2":
                listar_estudiantes(estudiantes)
            case "3":
                crear_curso(cursos)
            case "4":
                listar_cursos(cursos)
            case "5":
                inscribir_estudiante(estudiantes, cursos, inscripciones)
            case "6":
                registrar_nota(inscripciones, notas)
            case "7":
                resumen_academico(estudiantes, cursos, inscripciones, notas)
            case "8":
                break
            case _:
                print("Opción no válida.")


def menu_estudiante(cursos, inscripciones, notas):
    while True:
        print("\n===== MENÚ ESTUDIANTE =====")
        print("1. Listar cursos")
        print("2. Ver mis notas")
        print("3. Ver mis inscripciones")
        print("4. Ver estado académico")
        print("5. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                listar_cursos(cursos)
            case "2":
                ver_mis_notas(notas)
            case "3":
                ver_mis_inscripciones(inscripciones)
            case "4":
                estado_academico(notas)
            case "5":
                break
            case _:
                print("Opción no válida.")


def main():
    usuarios = []

    estudiantes = [
        {"id": 1, "nombre": "Juan Perez", "documento": "1001", "correo": "juan@correo.com", "semestre": "2"},
        {"id": 2, "nombre": "Laura Gomez", "documento": "1002", "correo": "laura@correo.com", "semestre": "3"},
        {"id": 3, "nombre": "Carlos Ruiz", "documento": "1003", "correo": "carlos@correo.com", "semestre": "1"}
    ]

    cursos = [
        {"id": 1, "nombre": "Programacion I", "profesor": "Andres Martinez", "cupos": 20},
        {"id": 2, "nombre": "Bases de Datos", "profesor": "Maria Rodriguez", "cupos": 15},
        {"id": 3, "nombre": "Matematicas", "profesor": "Felipe Torres", "cupos": 25}
    ]

    inscripciones = [
        {"id_estudiante": 1, "id_curso": 1},
        {"id_estudiante": 2, "id_curso": 2}
    ]

    notas = [
        {"id_estudiante": 1, "id_curso": 1, "nota": 4.5},
        {"id_estudiante": 2, "id_curso": 2, "nota": 3.9}
    ]

    while True:
        usuario_actual = None

        while usuario_actual is None:
            print("\n===== MENÚ PRINCIPAL =====")
            print("1. Crear usuario")
            print("2. Iniciar sesión")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    registrar_usuario(usuarios)
                case "2":
                    if len(usuarios) == 0:
                        print("Primero debe crear un usuario.")
                    else:
                        usuario_actual = login(usuarios)
                case "3":
                    print("Saliendo...")
                    return
                case _:
                    print("Opción no válida.")

        if usuario_actual["rol"] == "PROFESOR":
            menu_profesor(estudiantes, cursos, inscripciones, notas)
        else:
            menu_estudiante(cursos, inscripciones, notas)


if __name__ == "__main__":
    main()