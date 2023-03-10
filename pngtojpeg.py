from PIL import Image
import os

# Directorio donde se encuentran los archivos PNG a convertir
input_dir = '   '

# Directorio donde se guardarán los archivos JPEG convertidos
output_dir = 'C:/Users/Antonio/Downloads/midjourney_selection_2023-2-15_172755_[499]/jpeg'

# Recorrer el directorio y convertir los archivos PNG a JPEG
for filename in os.listdir(input_dir):
    if filename.endswith('.png'):
        # Abrir la imagen y convertirla a JPEG
        png_path = os.path.join(input_dir, filename)
        image = Image.open(png_path)
        jpeg_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.jpeg')
        image.convert('RGB').save(jpeg_path, 'JPEG')

print('La conversión ha sido completada.')