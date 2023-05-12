import os
import time
from tkinter import *
from tkinter import filedialog
import pygame.mixer
from PIL import Image, ImageTk, ImageSequence


def extraer_dato_lb1(dato1):
    seleccion = list_box_canciones.curselection()
    if len(seleccion) > 0:
        indice = int(seleccion[0])
        dato1 = list_box_canciones.get(indice)
        return dato1


def seleccionar():
    filename = filedialog.askopenfilename(title="Selecciona una canción", filetypes=[("Todos los archivos", "*.*")])
    lista.append(filename)
    pygame.mixer.music.load(filename)


def play():
    pygame.mixer.music.load(f'canciones/{extraer_dato_lb1(list_box_canciones.get(ACTIVE))}')
    pygame.mixer.music.play(loops=0)
    play_gif()


def pause():
    pygame.mixer.music.pause()


def stop():
    pygame.mixer.music.stop()


def play_gif():
    img = Image.open('image/rickroll.gif')
    for img in ImageSequence.Iterator(img):
        img = ImageTk.PhotoImage(img)
        gif_label.config(image=img)
        root.update()
        time.sleep(0.015)
    root.after(0, play_gif)


root = Tk()
pygame.mixer.init()

root.geometry("500x650")

lista = []
count = 0
anim = None

# FileDialog - Barra Menú
menu = Menu(root)
root.config(menu=menu, background="#333333")

abrir = Menu(menu, tearoff=0)
abrir.add_command(label="Importar...", command=seleccionar)
menu.add_cascade(label="Archivo", menu=abrir)

# GIF DECORACIÓN
file = PhotoImage(file='image/rickroll_art.png')

gif_label = Label(root, image=file, background='#333333')
gif_label.pack(pady=20, expand=True, fill='both')

# List Box
list_box_canciones = Listbox(root, width=40, background='#999999', border=10, highlightthickness=5, highlightbackground='#999999')
list_box_canciones.pack(padx=20, expand=True, fill='both')

list_box_canciones.bind("<<ListboxSelect>>", lambda event: extraer_dato_lb1(list_box_canciones.get(ACTIVE)))

for i in os.listdir('canciones'):
    list_box_canciones.insert(END, i)

# Frame
botones = Frame(root, background='#333333')
botones.pack(pady=20)

# Botones
boton1_png = PhotoImage(file='image/atras_40x40.png')
boton1 = Button(botones, text="Anterior", image=boton1_png, background='#999999', highlightthickness=0, border=5)
boton1.grid(row=0, column=0, padx=10)

boton2_png = PhotoImage(file='image/play_40x40.png')
boton2 = Button(botones, text="Play", command=play, image=boton2_png, background='#999999', highlightthickness=0, border=5)
boton2.grid(row=0, column=1, padx=10)

boton3_png = PhotoImage(file='image/pausa_40x40.png')
boton3 = Button(botones, text="Pause", command=pause, image=boton3_png, background='#999999', highlightthickness=0, border=5)
boton3.grid(row=0, column=2, padx=10)

boton4_png = PhotoImage(file='image/stop_40x40.png')
boton4 = Button(botones, text="Stop", command=stop, image=boton4_png, background='#999999', highlightthickness=0, border=5)
boton4.grid(row=0, column=3, padx=10)

boton5_png = PhotoImage(file='image/siguiente_40x40.png')
boton5 = Button(botones, text="Siguiente", image=boton5_png, background='#999999', highlightthickness=0, border=5)
boton5.grid(row=0, column=4, padx=10)

root.mainloop()
