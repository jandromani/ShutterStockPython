import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D
import keras.backend as K

def main():
    # Abre una ventana de diálogo para seleccionar la imagen de entrada
    root = tk.Tk()
    root.withdraw()
    in_path = filedialog.askopenfilename(title='Seleccionar imagen de entrada', filetypes=[('Archivos PNG', '*.png')])
    if not in_path:
        return

    # Carga la imagen de entrada y la convierte en un array NumPy
    img = Image.open(in_path)
    img_arr = np.array(img)

    # Define la arquitectura del modelo SRCNN
    model = Sequential()
    model.add(Conv2D(64, (9, 9), activation='relu', padding='same', input_shape=(None, None, 3)))
    model.add(Conv2D(32, (1, 1), activation='relu', padding='same'))
    model.add(Conv2D(3, (5, 5), activation='linear', padding='same'))

    # Carga los pesos pre-entrenados del modelo
    model.load_weights('srcnn_weights.h5')

    # Cuadriplica la imagen utilizando el modelo SRCNN
    img_arr = img_arr.astype('float32') / 255.
    y = model.predict(np.expand_dims(img_arr, axis=0))
    y = np.squeeze(y) * 255.
    y = np.clip(y, 0, 255).astype('uint8')

    # Crea una nueva imagen PIL a partir del array NumPy cuadriplicado
    out_img = Image.fromarray(y)

    # Abre una ventana de diálogo para guardar la imagen de salida con un prefijo "4x_"
    out_path = filedialog.asksaveasfilename(title='Guardar imagen cuadriplicada', defaultextension='.png', initialfile='4x_' + os.path.basename(in_path))
    if not out_path:
        return

    # Guarda la imagen de salida
    out_img.save(out_path)
    messagebox.showinfo('Proceso finalizado', 'La imagen se ha cuadriplicado con éxito.')

if __name__ == '__main__':
    main()