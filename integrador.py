def pedir_numero(mensaje):
    while True:
        try:
            cantidad = int(input(mensaje))
            if cantidad < 0:
                print("Ingrese un numero mayor o igual a cero")
            else:
                break
        except ValueError:
            print("Debe ingresar un numero")
    return cantidad

def pedir_numero_limite(mensaje, num_min, num_max, mensaje_limite):
    #hasta que el numero sea menor o igual a num_max y mayor o igual a num_min
    numero = num_max + 1
    while numero > num_max or numero < num_min:
        numero = pedir_numero(mensaje)
        if numero > num_max or numero < num_min:
            print(mensaje_limite)
    return numero

def pedir_palabra(mensaje):
    palabra = ""
    while palabra == "":
        palabra = input(mensaje).strip().capitalize()
    return palabra

def limpiar_nombre(nombre):
    return (
        nombre.lower()
        .replace('á', 'a')
        .replace('é', 'e')
        .replace('í', 'i')
        .replace('ó', 'o')
        .replace('ú', 'u')
    )

def pais_existe(nombre_pais, dataset):
    for pais in dataset:
        if nombre_pais == pais["nombre"]:
            return True
    return False

def mostrar_pais(pais):
    print(f"{pais['nombre']} (Poblacion = {pais['poblacion']}, Superficie = {pais['superficie']}, Continente = {pais['continente']})")


def pedir_pais_existente(dataset):
    while True:
        nombre = pedir_palabra("Ingrese el nombre del pais: ")
        encontrado = pais_existe(nombre, dataset)
        if encontrado:
            return nombre
        print(f"El pais {nombre} no existe en el dataset.")

def pedir_nuevo_pais(dataset):
    while True:
        nombre = pedir_palabra("Ingrese el nombre del pais: ")
        encontrado = pais_existe(nombre, dataset)
        if not encontrado:
            poblacion = pedir_numero("Ingrese la poblacion del pais: ")
            superficie = pedir_numero("Ingrese la superficie del pais: ")
            continente = pedir_palabra("Ingrese el continente del pais: ")
            pais = {
                "nombre": nombre,
                "poblacion": int(poblacion),
                "superficie": float(superficie),
                "continente": continente
            }
            return pais
        print(f"El pais {nombre} ya existe en el dataset.")

def cargar_dataset(dataset):
    with open("dataset.csv", "r") as f:
        encabezado_visto = False
        for linea in f:
            if not encabezado_visto:
                encabezado_visto = True
                continue
            nombre, poblacion, superficie, continente = linea.strip().split(",")
            try:
                dataset.append({
                    "nombre": nombre,
                    "poblacion": int(poblacion),
                    "superficie": float(superficie),
                    "continente": continente
                })
            except ValueError:
                print('No se pudo leer el dataset.')
                exit(1)
    print(f"Se cargaron {len(dataset)} paises exitosamente.")

def mostrar_dataset(dataset):
    for pais in dataset:
        mostrar_pais(pais)

def agregar_pais(dataset):
    pais = pedir_nuevo_pais(dataset)
    dataset.append(pais)
    print("El pais fue agregado correctamente.")

def actualizar_poblacion_superficie(dataset):
    nombre_pais = pedir_pais_existente(dataset)
    for pais in dataset:
        if nombre_pais == pais['nombre']:
            nueva_poblacion = pedir_numero("Ingrese la poblacion del pais: ")
            nueva_superficie = pedir_numero("Ingrese la superficie del pais: ")
            pais['poblacion'] = nueva_poblacion
            pais['superficie'] = nueva_superficie
    print(f"El pais {nombre_pais} ha sido actualizado correctamente")

def buscar_pais(dataset):
    nombre_parcial = pedir_palabra("Ingrese el nombre completo o parcial del pais: ").lower()
    coincidencias = False
    for pais in dataset:
        if limpiar_nombre(nombre_parcial) in limpiar_nombre(pais['nombre']):
            coincidencias = True
            mostrar_pais(pais)
    if not coincidencias:
        print(f"No se encontraron paises con {nombre_parcial}")

def filtrar_por_continente(dataset):
    continente = pedir_palabra("Ingrese el continente: ")
    coincidencias = False
    for pais in dataset:
        if limpiar_nombre(pais['continente']) == limpiar_nombre(continente):
            coincidencias = True
            mostrar_pais(pais)
    if not coincidencias:
        print(f"No se encontraron paises con el continente {continente}")

def filtrar_por_criterio_numerico(dataset, criterio):
    minimo = pedir_numero(f"Ingrese el valor minimo: ")
    maximo = pedir_numero(f"Ingrese el valor maximo: ")
    coincidencias = False
    for pais in dataset:
        if minimo <= pais[criterio] and pais[criterio] <= maximo:
            coincidencias = True
            mostrar_pais(pais)
    if not coincidencias:
        print(f"No se encontraron paises con {criterio} entre {minimo} y {maximo}")

def filtrar_paises(dataset):
    print("1. filtrar por continente")
    print("2. filtrar por rango de poblacion")
    print("3. filtrar por rango de superficie")
    opcion = pedir_numero_limite("Ingrese una opcion: ", 1, 3, "Ingrese una opcion entre 1 y 3")
    if opcion == 1:
        filtrar_por_continente(dataset)
    elif opcion == 2:
        filtrar_por_criterio_numerico(dataset, 'poblacion')
    else:
        filtrar_por_criterio_numerico(dataset, 'superficie')

def ordenar_por_criterio(dataset, criterio, desc):
    def obtener_criterio(pais):
        return pais[criterio]
    paises_ordenados = sorted(dataset, key=obtener_criterio, reverse=desc)
    for pais in paises_ordenados:
        mostrar_pais(pais)

def ordenar_paises(dataset):
    print("1. ordenar por nombre")
    print("2. ordenar por poblacion (ascendiente)")
    print("3. ordenar por poblacion (descendiente)")
    print("4. ordenar por superficie (ascendiente)")
    print("5. ordenar por superficie (descendiente)")
    opcion = pedir_numero_limite("Ingrese una opcion: ", 1, 5, "Ingrese una opcion entre 1 y 5")
    if opcion == 1:
        ordenar_por_criterio(dataset, 'nombre', False)
    elif opcion == 2:
        ordenar_por_criterio(dataset, 'poblacion', False)
    elif opcion == 3:
        ordenar_por_criterio(dataset, 'poblacion', True)
    elif opcion == 4:
        ordenar_por_criterio(dataset, 'superficie', False)
    else:
        ordenar_por_criterio(dataset, 'superficie', True)

def obtener_pais_mayor_poblacion(dataset):
    maximo_pais = dataset[0]
    for pais in dataset:
        if pais['poblacion'] > maximo_pais['poblacion']:
            maximo_pais = pais
    return maximo_pais

def obtener_pais_menor_poblacion(dataset):
    minimo_pais = dataset[0]
    for pais in dataset:
        if pais['poblacion'] < minimo_pais['poblacion']:
            minimo_pais = pais
    return minimo_pais

def obtener_promedio_criterio(dataset, criterio):
    suma = 0
    promedio = dataset[0][criterio]
    for pais in dataset:
        suma = suma + pais[criterio]
    promedio = suma / len(dataset)
    return promedio

def obtener_paises_por_continente(dataset):
    paises_por_continente = {}
    for pais in dataset:
        if pais['continente'] in paises_por_continente:
            paises_por_continente[pais['continente']] += 1
        else:
            paises_por_continente[pais['continente']] = 1
    return paises_por_continente

def mostrar_estadisticas(dataset):
    if len(dataset) == 0:
        print("No hay paises en el dataset.")
        return
    pais_mayor_poblacion = obtener_pais_mayor_poblacion(dataset)
    pais_menor_poblacion = obtener_pais_menor_poblacion(dataset)
    promedio_poblacion = obtener_promedio_criterio(dataset, 'poblacion')
    promedio_superficie = obtener_promedio_criterio(dataset, 'superficie')
    paises_por_continente = obtener_paises_por_continente(dataset)

    print(f"Pais con mayor poblacion: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']})")
    print(f"Pais con menor poblacion: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']})")
    print(f"Promedio de poblacion: {promedio_poblacion}")
    print(f"Promedio de superficie: {promedio_superficie}")
    print(f"\nPaises por continente")
    for continente in paises_por_continente:
        print(f"{continente}: {paises_por_continente[continente]}")

def mostrar_menu():
    print("1. cargar dataset")
    print("2. mostrar dataset")
    print("3. agregar pais")
    print("4. actualizar pais")
    print("5. buscar pais")
    print("6. filtrar paises")
    print("7. ordenar paises")
    print("8. mostrar estadisticas")
    print("9. salir")

dataset = []
opcion = 0
while opcion != 9:
    mostrar_menu()
    opcion = pedir_numero_limite("Ingrese una opcion: ", 1, 9, "Ingrese una opcion entre 1 y 9")
    if opcion == 1:
        cargar_dataset(dataset)
    elif opcion == 2:
        mostrar_dataset(dataset)
    elif opcion == 3:
        agregar_pais(dataset)
    elif opcion == 4:
        actualizar_poblacion_superficie(dataset)
    elif opcion == 5:
        buscar_pais(dataset)
    elif opcion == 6:
        filtrar_paises(dataset)
    elif opcion == 7:
        ordenar_paises(dataset)
    elif opcion == 8:
        mostrar_estadisticas(dataset)

