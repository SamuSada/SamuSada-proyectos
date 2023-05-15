import time
import os
import pygame.mixer
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageSequence


def extraer_dato_lb1(dato1):
    seleccion = listbox1.curselection()
    if len(seleccion) > 0:
        indice = int(seleccion[0])
        dato1 = listbox1.get(indice)
        return dato1


def play():
    pygame.mixer.music.load(f'{ruta}/{extraer_dato_lb1(listbox1.get(ACTIVE))}')
    pygame.mixer.music.play(loops=0)


def pause():
    pygame.mixer.music.pause()


def stop():
    pygame.mixer.music.stop()


def siguiente():
    pass


def seleccionar_dir():
    ruta = filedialog.askdirectory()
    for i in os.listdir(ruta):
        listbox1.insert(END, i)


ruta = "canciones"

pygame.mixer.init()

root = Tk()
root.minsize(500, 450)
root.maxsize(500, 450)

# MENU ARRIBA
menu = Menu(root)
root.config(menu=menu, background="#333333")

abrir = Menu(menu, tearoff=0)
abrir.add_command(label="Importar...", command=seleccionar_dir)
menu.add_cascade(label="Archivo", menu=abrir)

# MARCO LISTBOX PNG
marco_png = PhotoImage(file='image/frame.png')
frame1 = Canvas(root, width=495, height=407, background='#333333', highlightthickness=0)
frame1.create_image(245, 151, image=marco_png)
frame1.place(x=1, y=0)

# LISTBOX
listbox1 = Listbox(root, width=40, border=10, background='#999999')
listbox1.pack(padx=20, pady=40)
listbox1.bind("<<ListboxSelect>>", lambda event: extraer_dato_lb1(listbox1.get(ACTIVE)))
# for i in os.listdir('canciones'):
#     listbox1.insert(END, i)

# BOTONES
botones = Frame(root, background='#333333')
botones.pack(padx=20, pady=20)

boton1_png = PhotoImage(file='image/atras_40x40.png')
boton1 = Button(botones, text="Anterior", image=boton1_png, background='#999999', highlightthickness=0, border=5)
boton1.grid(row=0, column=0, padx=10)

boton2_png = PhotoImage(file='image/play_40x40.png')
boton2 = Button(botones, text="Play", image=boton2_png, background='#999999', highlightthickness=0, border=5, command=play)
boton2.grid(row=0, column=1, padx=10)

boton3_png = PhotoImage(file='image/pausa_40x40.png')
boton3 = Button(botones, text="Pause", image=boton3_png, background='#999999', highlightthickness=0, border=5, command=pause)
boton3.grid(row=0, column=2, padx=10)

boton4_png = PhotoImage(file='image/stop_40x40.png')
boton4 = Button(botones, text="Stop", image=boton4_png, background='#999999', highlightthickness=0, border=5)
boton4.grid(row=0, column=3, padx=10)

boton5_png = PhotoImage(file='image/siguiente_40x40.png')
boton5 = Button(botones, text="Siguiente", image=boton5_png, background='#999999', highlightthickness=0, border=5, command=siguiente)
boton5.grid(row=0, column=4, padx=10)


root.mainloop()

