import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pygame

root = tk.Tk()
root.title("Win Hampa")
root.geometry("300x200")

pygame.init()

def buscar_archivo():
    filepath = filedialog.askopenfilename(filetypes=[("Archivos audio", "*.mp3"), ("Archivos Vídeo", "*.mp4")])
    reproducir(filepath)

def reproducir(filepath):
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()

def pausar():
    pygame.mixer.music.pause()

def continuar():
    pygame.mixer.music.unpause()

def paral():
    pygame.mixer.music.stop()


browse_button = tk.Button(root, text="Explorar", command=buscar_archivo)
browse_button.pack()

pause_button = tk.Button(root, text="Pausa", command=pausar)
pause_button.pack()

resume_button = tk.Button(root, text="Continuar", command=continuar)
resume_button.pack()

stop_button = tk.Button(root, text="Paralse", command=paral)
stop_button.pack()

root.mainloop()
