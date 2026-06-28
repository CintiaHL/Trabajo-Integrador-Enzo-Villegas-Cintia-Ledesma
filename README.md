# Gestión de Datos de Países en Python

Trabajo Práctico Integrador — Programación 1

**Institución:** UNIVERSIDAD TECNOLÓGICA NACIONAL - FACULTAD REGIONAL SAN NICOLÁS
**Carrera:** TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN
**Materia:** Programación 1  
**Integrantes:** Enzo Villegas, Cintia Ledesma

## Descripción

Aplicación de consola desarrollada en Python que permite gestionar información sobre países. El sistema lee datos desde un archivo CSV y ofrece funcionalidades de consulta, filtrado, ordenamiento y estadísticas sobre el dataset.

## Requisitos

- Python 3.x

## Instrucciones de uso

1. Clonar el repositorio.
2. Asegurarse de que el archivo `dataset.csv` se encuentre en la misma carpeta que `integrador.py`.
3. Ejecutar el programa:

```bash
python integrador.py
```

4. Se mostrará un menú con las siguientes opciones:

```
1. cargar dataset
2. mostrar dataset
3. agregar pais
4. actualizar pais
5. buscar pais
6. filtrar paises
7. ordenar paises
8. mostrar estadisticas
9. salir
```

**Importante:** La primera acción debe ser **cargar el dataset** (opción 1) para que el programa tenga datos con los que trabajar.

## Funcionalidades

- **Cargar dataset:** Lee los países desde `dataset.csv`.
- **Mostrar dataset:** Lista todos los países cargados con su información.
- **Agregar país:** Permite ingresar un nuevo país con nombre, población, superficie y continente. No permite campos vacíos ni países duplicados.
- **Actualizar país:** Modifica la población y superficie de un país existente.
- **Buscar país:** Busca por nombre completo o parcial (insensible a mayúsculas y acentos).
- **Filtrar países:** Filtra por continente, rango de población o rango de superficie.
- **Ordenar países:** Ordena por nombre, población o superficie (ascendente o descendente).
- **Estadísticas:** Muestra el país con mayor y menor población, promedios de población y superficie, y cantidad de países por continente.

## Formato del archivo CSV

El archivo `dataset.csv` debe tener el siguiente formato:

```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

## Ejemplos de entrada/salida

### Cargar dataset
```
Ingrese una opcion: 1
Se cargaron 4 paises exitosamente.
```

### Buscar país (coincidencia parcial)
```
Ingrese una opcion: 5
Ingrese el nombre completo o parcial del pais: arg
Argentina (Poblacion = 45376763, Superficie = 2780400.0, Continente = América)
```

### Filtrar por continente
```
Ingrese una opcion: 6
1. filtrar por continente
2. filtrar por rango de poblacion
3. filtrar por rango de superficie
Ingrese una opcion: 1
Ingrese el continente: América
Argentina (Poblacion = 45376763, Superficie = 2780400.0, Continente = América)
Brasil (Poblacion = 213993437, Superficie = 8515767.0, Continente = América)
```

### Estadísticas
```
Ingrese una opcion: 8
Pais con mayor poblacion: Brasil (213993437)
Pais con menor poblacion: Argentina (45376763)
Promedio de poblacion: 117079875.0
Promedio de superficie: 2920291.0
Paises por continente
América: 2
Asia: 1
Europa: 1
```

## Participación de los integrantes

| Integrante | Participación |
|------------|---------------|
| Enzo       | Desarrollo del código fuente, testing y documentación |
| Cintia     | Desarrollo del código fuente, testing y documentación |

## Enlaces

- **Video demostrativo:** https://youtu.be/e3Wu8Dh6jKo
- **Documentación (PDF):** https://github.com/CintiaHL/Trabajo-Integrador-Enzo-Villegas-Cintia-Ledesma)
