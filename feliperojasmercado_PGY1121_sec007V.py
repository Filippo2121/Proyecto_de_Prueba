import numpy as np

# Lista lotes
lotes = [
    {'numero': '1', 'tamaño': '100 m2', 'precio': '$230,000'},
    {'numero': '2', 'tamaño': '150 m2', 'precio': '$360,000'},
    {'numero': '3', 'tamaño': '120 m2', 'precio': '$150,000'},
    {'numero': '4', 'tamaño': '200 m2', 'precio': '$500,000'}
]

# Definir matriz de lotes disponibles.
lotes_disponibles = np.array([[1, 2, 3, 4]])

# Lista de lotes seleccionados por cliente 
lotes_seleccionados = []

# Funcion para mostrar la disponibilidad de lotes del cliente 
def mostrar_disponibilidad_lotes():
    print("Lotes Disponibles:")
    for fila in lotes_disponibles:
        for lote in fila:
            if lote == 0:
                print("[1,2,3,4]", end=" ")
            else:
                print("[ ]", end=" ")
        print()

# seleccionar un lote
def seleccionar_lote():
    rut = input("Ingrese su RUT: ")
    nombre = input("Ingrese su nombre completo: ")
    telefono = input("Ingrese su telefono: ")
    email = input("Ingrese su email: ")
    fila = int(input("Ingrese la fila del lote: "))
    columna = int(input("Ingrese la columna del lote: "))

    # Validar coordenadas de lote
    if fila < 0 or fila >= lotes_disponibles.shape[0] or columna < 0 or columna >= lotes_disponibles.shape[1]:
        print("Coordenadas invalidas. Por favor, ingrese coordenadas validas.")
        return

    # Disponibilidad de lote
    if lotes_disponibles[fila, columna] == 0:
        print("El lote seleccionado no esta disponible.")
    else:
        # Guardar los detalles del cliente y marcar el lote como vendido
        lotes_seleccionados.append({
            'RUT': rut,
            'Nombre': nombre,
            'Telefono': telefono,
            'Email': email,
            'Fila': fila,
            'Columna': columna
        })
        lotes_disponibles[fila, columna] = 0
        print("Lote seleccionado correctamente.")

# mostrar detalles de lote seleccionado
def mostrar_detalles_lote():
    if len(lotes_seleccionados) == 0:
        print("No hay lotes seleccionados.")
    else:
        for lote in lotes_seleccionados:
            fila = lote['Fila']
            columna = lote['Columna']
            numero_lote = lotes_disponibles[fila, columna]
            print(f"Detalles del lote seleccionado:")
            print(f"Numero de lote: {numero_lote}")
            print(f"Tamaño del terreno: {calcular_tamaño_terreno(numero_lote)}")
            print(f"Precio: {calcular_precio(numero_lote)}")
            print(f"RUT: {lote['RUT']}")
            print(f"Nombre: {lote['Nombre']}")
            print(f"Telefono: {lote['Telefono']}")
            print(f"Email: {lote['Email']}")
            print()

# mostrar la lista de clientes que a comprado un lote
def mostrar_clientes():
    if len(lotes_seleccionados) == 0:
        print("No hay clientes registrados.")
    else:
        print("Clientes que han comprado un lote:")
        for lote in lotes_seleccionados:
            print(f"RUT: {lote['RUT']}")
            print(f"Nombre: {lote['Nombre']}")
            print()

# calcular el tamaño del terreno de un lote
def calcular_tamaño_terreno(numero_lote):
    for lote in lotes:
        if lote['numero'] == str(numero_lote):
            return lote['tamaño']
    return "Desconocido"

# Funcion para calcular precio de lote
def calcular_precio(numero_lote):
    for lote in lotes:
        if lote['numero'] == str(numero_lote):
            return lote['precio']
    return "Desconocido"

# Ejecucion de el menu
def ejecutar_menu():
    while True:
        print("----- Menú -----")
        print("1. Ver disponibilidad de lotes")
        print("2. Seleccionar un lote")
        print("3. Ver detalles del lote seleccionado")
        print("4. Ver clientes")
        print("5. Salir")

        opcion = input("Ingrese una opcion: ")

        if opcion == '1':
            mostrar_disponibilidad_lotes()
        elif opcion == '2':
            seleccionar_lote()
        elif opcion == '3':
            mostrar_detalles_lote()
        elif opcion == '4':
            mostrar_clientes()
        elif opcion == '5':
            print("Gracias por utilizar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción invalida. Por favor, ingrese una opcion valida.")

# Ejecutar el menu
ejecutar_menu()