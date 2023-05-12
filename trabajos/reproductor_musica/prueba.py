from pygame import mixer
import pygame.mixer

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('canciones/1-01Opening.mp3')
pygame.mixer.music.play(loops=1)


