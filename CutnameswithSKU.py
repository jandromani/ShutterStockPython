import os
import re

directory = 'C:/Users/Antonio/Downloads/midjourney_selection_2023-2-15_124825_[321]' # Reemplaza con la ruta a tu directorio
pattern = r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}'

# Crear una expresión regular que encuentre el patrón al final del nombre del archivo
regex_pattern = re.compile(f"_{pattern}\.(\w+)$")

# Crear un diccionario para hacer un seguimiento de los nombres de archivo y su número secuencial
names_dict = {}

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    
    # Comprobar si el archivo contiene el patrón y modificar su nombre si es necesario
    if re.search(pattern, filename):
        new_filename = regex_pattern.sub('_1.\\1', filename)
        i = 1
        while new_filename in names_dict:
            i += 1
            new_filename = regex_pattern.sub(f'_{i}.\\1', filename)
        os.rename(filepath, os.path.join(directory, new_filename))
        names_dict[new_filename] = i
        
    # Si el archivo no contiene el patrón, agregar su nombre al diccionario
    else:
        names_dict[filename] = 0

print(names_dict)