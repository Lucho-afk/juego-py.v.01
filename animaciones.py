import pygame, sys, random
from pygame.locals import *

pygame.init()

color=(255,255,255)
red=(255,0,0)
tam=(500,500)
pantalla=pygame.display.set_mode(tam)
clock=pygame.time.Clock()

copos_sangrientos=[]
for i in range(60):
    #importar libreria random, randint lo que hace es enviar al azar un numero entre los rangos
    x=random.randint(0,800)
    y=random.randint(0,500)
    copos_sangrientos.append ([x,y])

while True:
    #sistema para salir del juego
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            sys.exit()

    pantalla.fill(color)
    for i in copos_sangrientos:
    #importar libreria random, randint lo que hace es enviar al azar un numero entre los rangos

        pygame.draw.circle(pantalla, red,i,2)
        i[1]+=1
        if i[1]>500:
            i[1]=0

    pygame.display.update()
    clock.tick(30)
