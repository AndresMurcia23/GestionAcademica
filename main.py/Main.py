def registrar_usuario(usuarios):
    """
    Registra un nuevo usuario dentro del sistema académico.

    Esta función solicita por consola un nickname y una contraseña,
    valida que el nickname no exista previamente en la colección de usuarios
    y permite asignar un rol específico al usuario (ESTUDIANTE o PROFESOR).

    Parámetros:
    ----------
    usuarios : list
        Lista de diccionarios que almacena la información de los usuarios.

    Retorna:
    -------
    None

    Consideraciones técnicas:
    ------------------------
    - Utiliza listas y diccionarios como estructuras contenedoras.
    - Modifica directamente la lista recibida por referencia.
"""
    
    print("\n===== CREAR USUARIO =====")

    nickname = input("Cree su nickname: ")
    contraseña = input("Cree su contraseña: ")

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
        "contraseña": contraseña,
        "rol": rol
    }

    usuarios.append(nuevo_usuario)

    print("\nUsuario creado correctamente.")
    print(f"Rol asignado: {rol}")


def login(usuarios):
    """
    Realiza el proceso de autenticación de usuarios.

    La función solicita credenciales por consola y verifica si
    existe un usuario registrado con los datos ingresados.

    Parámetros:
    ----------
    usuarios : list
        Colección de usuarios registrados en el sistema.

    Retorna:
    -------
    dict | None
        Retorna el diccionario correspondiente al usuario autenticado
        si las credenciales son válidas. En caso contrario, retorna None.

    Consideraciones técnicas:
    ------------------------
    - Accede a estructuras tipo diccionario mediante claves.
    - Utiliza retorno condicional para control de flujo.
    """
    print("\n===== LOGIN =====")

    nickname = input("Digite su nickname: ")
    contraseña = input("Digite su contraseña: ")

    for usuario in usuarios:
        if usuario["nickname"] == nickname and usuario["contraseña"] == contraseña:
            print("\nInicio de sesión exitoso.")
            print(f"Bienvenido {usuario['nickname']}")
            print(f"Rol: {usuario['rol']}")
            return usuario

    print("\nUsuario o contraseña incorrectos.")
    return None


def crear_estudiante(estudiantes):
    """
    Crea y registra un nuevo estudiante en el sistema.

    Solicita información básica del estudiante y genera automáticamente
    un identificador basado en el tamaño actual de la colección.

    Parámetros:
    ----------
    estudiantes : list
        Lista que almacena los estudiantes registrados.

    Retorna:
    -------
    None

    Consideraciones técnicas:
    ------------------------
    - Utiliza estructuras de datos tipo diccionario.
    - Genera IDs incrementales mediante len().
    - Inserta elementos dinámicamente en memoria.
    """

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
    """
    Muestra en consola todos los estudiantes registrados.

    Recorre secuencialmente la colección de estudiantes e imprime
    la información almacenada de cada entidad.

    Parámetros:
    ----------
    estudiantes : list
        Lista de estudiantes registrados.

    Retorna:
    -------
    None

    Consideraciones técnicas:
    ------------------------
    - Implementa recorrido secuencial O(n).
    - Accede a datos mediante claves de diccionario.
    - Realiza validación de colección vacía.
    """
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
    """
    Registra un nuevo curso académico.

    Solicita información relacionada con el curso y valida
    la entrada numérica correspondiente a los cupos disponibles.

    Parámetros:
    ----------
    cursos : list
        Lista de cursos almacenados en memoria.

    Retorna:
    -------
    None

    Consideraciones técnicas:
    ------------------------
    - Implementa conversión de tipos str → int.
    - Utiliza manejo de excepciones con try-except.
    - Almacena información utilizando diccionarios.
    """
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
    """
    Visualiza todos los cursos registrados en el sistema.

    Parámetros:
    ----------
    cursos : list
        Colección de cursos registrados.

    Retorna:
    -------
    None

    Consideraciones técnicas:
    ------------------------
    - Implementa iteración secuencial O(n).
    - Realiza validación de lista vacía.
    - Utiliza formateo dinámico mediante f-strings.
    """
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
    """
    Realiza el proceso de inscripción de un estudiante en un curso.

    La función valida la existencia del estudiante y del curso,
    verifica disponibilidad de cupos y evita duplicidad
    de inscripciones.

    Parámetros:
    ----------
    estudiantes : list
        Colección de estudiantes.

    cursos : list
        Colección de cursos disponibles.

    inscripciones : list
        Registro de inscripciones realizadas.

    Retorna:
    -------
    None

    Consideraciones técnicas:
    ------------------------
    - Implementa múltiples recorridos secuenciales O(n).
    - Utiliza validaciones de integridad de datos.
    - Modifica estructuras mutables por referencia.
    - Aplica reglas de negocio para control de cupos.
    """

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

    if estudiante_existe == False:
        print("Error: El estudiante no existe.")
        return

    if curso_encontrado == None:
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
    """
    Registra múltiples calificaciones para estudiantes inscritos.

    Permite ingresar varias notas de manera consecutiva
    hasta que el usuario decida finalizar el proceso.

    Parámetros:
    ----------
    inscripciones : list
        Lista de estudiantes inscritos en cursos.

    notas : list
        Registro general de notas.

    Retorna:
    -------
    None
    """

    print("\n===== REGISTRAR NOTAS =====")

    if len(inscripciones) == 0:
        print("No hay estudiantes inscritos.")
        return

    
    while True:

        try:
            
            id_estudiante = int(input("\nIngrese el ID del estudiante: "))

            
            id_curso = int(input("Ingrese el ID del curso: "))

        except ValueError:
            print("Error: Debe ingresar números válidos.")
            continue

        
        esta_inscrito = False

        
        for inscripcion in inscripciones:

            
            if (
                inscripcion["id_estudiante"] == id_estudiante
                and inscripcion["id_curso"] == id_curso
            ):
                esta_inscrito = True

        
        if esta_inscrito == False:
            print("Error: El estudiante no está inscrito en ese curso.")
            continue

        try:
            
            nota = float(input("Ingrese la nota de 0.0 a 5.0: "))

        except ValueError:
            print("Error: Debe ingresar un valor numérico.")
            continue

        
        if nota < 0.0 or nota > 5.0:
            print("Error: La nota debe estar entre 0.0 y 5.0.")
            continue

        
        nueva_nota = {
            "id_estudiante": id_estudiante,
            "id_curso": id_curso,
            "nota": nota
        }

        
        notas.append(nueva_nota)

        print("\nNota registrada correctamente.")

        
        continuar = input("\n¿Desea registrar otra nota? (si/no): ").lower()

        
        if continuar != "si":
            print("\nFinalizando registro de notas...")
            break


def ver_mis_notas(notas):
    """
    Muestra las notas registradas en el sistema.

    Determina adicionalmente el estado académico
    del estudiante según la calificación obtenida.

    Parámetros:
    ----------
    notas : list
        Colección de notas registradas.

    Retorna:
    -------
    None

    Consideraciones técnicas:
    ------------------------
    - Implementa operador ternario.
    - Recorre estructuras dinámicas en memoria.
    - Utiliza validación de datos vacíos.
    """
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
    """
    Visualiza las inscripciones registradas en el sistema.

    Parámetros:
    ----------
    inscripciones : list
        Lista de inscripciones activas.

    Retorna:
    -------
    None

    Consideraciones técnicas:
    ------------------------
    - Implementa recorrido secuencial.
    - Utiliza acceso a diccionarios mediante claves.
    """
    print("\n===== MIS INSCRIPCIONES =====")

    if len(inscripciones) == 0:
        print("No hay inscripciones registradas.")
        return

    for inscripcion in inscripciones:
        print(f"Estudiante ID: {inscripcion['id_estudiante']}")
        print(f"Curso ID: {inscripcion['id_curso']}")
        print("-----------------------------")


def estado_academico(notas):
    """
    Muestra el estado académico de los estudiantes
    según las notas registradas.

    Parámetros:
    ----------
    notas : list
        Colección de notas almacenadas.

    Retorna:
    -------
    None

    Consideraciones técnicas:
    ------------------------
    - Utiliza operadores condicionales.
    - Implementa lógica de evaluación académica.
    """
    print("\n===== ESTADO ACADÉMICO =====")

    if len(notas) == 0:
        print("No hay notas registradas.")
        return

    for nota in notas:
        estado = "Aprobado" if nota["nota"] >= 3.0 else "Reprobado"
        print(f"Curso ID: {nota['id_curso']} - Nota: {nota['nota']} - {estado}")


def resumen_academico(estudiantes, cursos, inscripciones, notas):
    """
    Genera un resumen general del estado académico del sistema.

    Calcula métricas relacionadas con estudiantes, cursos,
    inscripciones y promedio general de notas.

    Parámetros:
    ----------
    estudiantes : list
    cursos : list
    inscripciones : list
    notas : list

    Retorna:
    -------
    None

    Consideraciones técnicas:
    ------------------------
    - Implementa acumuladores.
    - Realiza cálculos estadísticos básicos.
    - Utiliza operaciones aritméticas sobre colecciones.
    """
    print("\n===== RESUMEN ACADÉMICO =====")

    print(f"Total de estudiantes: {len(estudiantes)}")
    print(f"Total de cursos: {len(cursos)}")
    print(f"Total de inscripciones: {len(inscripciones)}")
    print(f"Total de notas registradas: {len(notas)}")

    if len(notas) == 0:
        print("No hay notas para calcular aprobados o reprobados.")
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
    """
    Gestiona el menú interactivo correspondiente al rol PROFESOR.

    Permite acceder a las funcionalidades administrativas
    del sistema académico.

    Parámetros:
    ----------
    estudiantes : list
    cursos : list
    inscripciones : list
    notas : list

    Retorna:
    -------
    None

    Consideraciones técnicas:
    ------------------------
    - Implementa bucles infinitos controlados.
    - Utiliza pattern matching.
    - Centraliza navegación del sistema.
    """
    while True:
        print()
        print("╔════════════════════════════════════════════╗")
        print("║              MENÚ PROFESOR                ║")
        print("╠════════════════════════════════════════════╣")
        print("║  1. Crear estudiante                      ║")
        print("║  2. Listar estudiantes                    ║")
        print("║  3. Crear curso                           ║")
        print("║  4. Listar cursos                         ║")
        print("║  5. Inscribir estudiante                  ║")
        print("║  6. Registrar nota                        ║")
        print("║  7. Ver resumen académico                 ║")
        print("║  8. Cerrar sesión                         ║")
        print("╚════════════════════════════════════════════╝")

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
                print("\nCerrando sesión...")
                break
            case _:
                print("\nOpción no válida.")


def menu_estudiante(cursos, inscripciones, notas):
    """
    Gestiona el menú interactivo correspondiente al rol ESTUDIANTE.

    Permite consultar cursos, notas e información académica.

    Parámetros:
    ----------
    cursos : list
    inscripciones : list
    notas : list

    Retorna:
    -------
    None

    Consideraciones técnicas:
    ------------------------
    - Implementa control de flujo mediante match-case.
    - Utiliza navegación estructurada por consola.
    """
    while True:
        print()
        print("╔════════════════════════════════════════════╗")
        print("║             MENÚ ESTUDIANTE               ║")
        print("╠════════════════════════════════════════════╣")
        print("║  1. Listar cursos                         ║")
        print("║  2. Ver mis notas                         ║")
        print("║  3. Ver mis inscripciones                 ║")
        print("║  4. Ver estado académico                  ║")
        print("║  5. Cerrar sesión                         ║")
        print("╚════════════════════════════════════════════╝")

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
                print("\nCerrando sesión...")
                break
            case _:
                print("\nOpción no válida.")


def main():
    """
    Función principal del sistema académico.

    Inicializa las estructuras de almacenamiento en memoria,
    carga datos iniciales y controla el flujo principal
    de ejecución del programa.

    Retorna:
    -------
    None

    Consideraciones técnicas:
    ------------------------
    - Define estructuras de datos dinámicas.
    - Gestiona autenticación y control de roles.
    - Implementa bucles principales de ejecución.
    - Actúa como punto central de coordinación del sistema.
    """
    usuarios = []

    estudiantes = [
        {
            "id": 1,
            "nombre": "Juan Perez",
            "documento": "1001",
            "correo": "juan@correo.com",
            "semestre": "2"
        },
        {
            "id": 2,
            "nombre": "Laura Gomez",
            "documento": "1002",
            "correo": "laura@correo.com",
            "semestre": "3"
        },
        {
            "id": 3,
            "nombre": "Carlos Ruiz",
            "documento": "1003",
            "correo": "carlos@correo.com",
            "semestre": "1"
        }
    ]

    cursos = [
        {
            "id": 1,
            "nombre": "Programacion I",
            "profesor": "Andres Martinez",
            "cupos": 20
        },
        {
            "id": 2,
            "nombre": "Bases de Datos",
            "profesor": "Maria Rodriguez",
            "cupos": 15
        },
        {
            "id": 3,
            "nombre": "Matematicas",
            "profesor": "Felipe Torres",
            "cupos": 25
        }
    ]

    inscripciones = [
        {"id_estudiante": 1, "id_curso": 1},
        {"id_estudiante": 1, "id_curso": 3},
        {"id_estudiante": 2, "id_curso": 2},
        {"id_estudiante": 3, "id_curso": 1}
    ]

    notas = [
        {"id_estudiante": 1, "id_curso": 1, "nota": 4.2},
        {"id_estudiante": 1, "id_curso": 3, "nota": 3.8},
        {"id_estudiante": 2, "id_curso": 2, "nota": 4.6},
        {"id_estudiante": 3, "id_curso": 1, "nota": 2.9}
    ]

    while True:
        usuario_actual = None

        while usuario_actual == None:
            print()
            print("╔════════════════════════════════════════════╗")
            print("║              MENÚ DE ACCESO               ║")
            print("╠════════════════════════════════════════════╣")
            print("║  1. Crear usuario                         ║")
            print("║  2. Iniciar sesión                        ║")
            print("║  3. Salir                                 ║")
            print("╚════════════════════════════════════════════╝")

            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    registrar_usuario(usuarios)

                case "2":
                    if len(usuarios) == 0:
                        print("\nPrimero debe crear un usuario.")
                    else:
                        usuario_actual = login(usuarios)

                case "3":
                    print("\nGracias por usar el sistema.")
                    return

                case _:
                    print("\nOpción no válida.")

        if usuario_actual["rol"] == "PROFESOR":
            menu_profesor(estudiantes, cursos, inscripciones, notas)

        elif usuario_actual["rol"] == "ESTUDIANTE":
            menu_estudiante(cursos, inscripciones, notas)


if __name__ == "__main__":
    main()
