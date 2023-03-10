import os

# Especifica el directorio que quieres leer
directorio = "/ruta/del/directorio/"

# Crea una lista para almacenar los resultados
resultados = []

# Itera a través de cada archivo en el directorio
for archivo in os.listdir(directorio):
    # Verifica que el archivo sea un archivo y no un directorio
    if os.path.isfile(os.path.join(directorio, archivo)):
        # Extrae el nombre del archivo sin la extensión
        nombre_archivo, extension = os.path.splitext(archivo)
        # Agrega el nombre del archivo y la ruta a la lista de resultados
        resultados.append(nombre_archivo + "," + os.path.join(directorio, archivo))

# Imprime los resultados
for resultado in resultados:
    print(resultado)