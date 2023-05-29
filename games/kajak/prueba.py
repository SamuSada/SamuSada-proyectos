import sys
import pygame
import random
from pygame.locals import *


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super(Jugador, self).__init__()
        self.barca = pygame.image.load('images/kajak.gif').convert()
        self.barca.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.barca.get_rect()
        self.rect.x = 340
        self.rect.y = 400
        self.img_inv = pygame.transform.flip(self.barca, True, False)

    def update(self, tecla_pul):
        if tecla_pul[K_UP] or tecla_pul[K_w]:
            self.rect.move_ip(0, -5)
        if tecla_pul[K_DOWN] or tecla_pul[K_s]:
            self.rect.move_ip(0, 5)
        if tecla_pul[K_RIGHT] or tecla_pul[K_d]:
            self.rect.move_ip(5, 0)
        if tecla_pul[K_LEFT] or tecla_pul[K_a]:
            self.rect.move_ip(-5, 0)
            screen.fill((255, 255, 255))
            screen.blit(background, [0, 0])
            screen.blit(player.img_inv, player.rect)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 400:
            self.rect.top = 400
        if self.rect.bottom >= 500:
            self.rect.bottom = 500


class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemigo, self).__init__()
        self.surf = pygame.image.load('images/meteorito.png').convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(10, 790),
                -100
            )
        )
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.move_ip(random.randint(-1, 1), 2)
        if self.rect.right < 0:
            self.kill()


pygame.init()  # INICIO
screen = pygame.display.set_mode((800, 600))
PANTALLA_ANCHO = 800
PANTALLA_ALTO = 600
ejecutando = True
background = pygame.image.load('images/background.png').convert()
background_lose = pygame.image.load('images/background_lose.png').convert()
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
player = Jugador()
ADDEnemigo = pygame.USEREVENT + 1
pygame.time.set_timer(ADDEnemigo, 600)

enemigos = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# BUCLE DEL JUEGO
while ejecutando:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == ADDEnemigo:
            nuevo_enemigo = Enemigo()
            enemigos.add(nuevo_enemigo)
            all_sprites.add(nuevo_enemigo)

    # FONDO
    screen.fill((255, 255, 255))
    screen.blit(background, [0, 0])
    # COLOCAR OBJETO
    pulsacion = pygame.key.get_pressed()
    player.update(pulsacion)
    enemigos.update()
    screen.blit(player.barca, player.rect)

    clock.tick(60)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemigos):
        player.kill()
        screen.blit(background_lose, [0, 0])
        ejecutando = False
