import os
import csv

# Especifica el directorio donde se encuentran los archivos
directory = "C:/Users/Antonio/Downloads/midjourney_selection_2023-2-15_172755_[499]"

# Crea una lista vacía para guardar los datos
data = []

# Itera sobre los archivos en el directorio
for filename in os.listdir(directory):
    if filename.endswith(".png"):  # Solo considera los archivos con extensión .jpg
        filepath = os.path.join(directory, filename)
        name = os.path.splitext(filename)[0]  # Obtiene el nombre del archivo sin extensión
        sku = name + "-SKU"  # Genera un SKU único para el archivo
        mpn = name + "-MPN"  # Genera un MPN único para el archivo
        price = "24.99 USD"  # Especifica el precio
        brand = "Gallery-Hub"  # Especifica la marca
        row = [name, filepath, sku, mpn, price, brand]  # Crea una lista con los datos del archivo
        data.append(row)  # Agrega la lista a la lista general de datos

# Guarda los datos en un archivo CSV
with open("datos.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)