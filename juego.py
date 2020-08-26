import pygame, sys
from pygame.locals import *

rojo=(255,0,0)#se pueden crear colores por medio de una tupla
verde=(0,255,0)
azul=(0,0,255)
amarillo=(255,255,0)
morado=(255,0,255)
lista=[rojo,verde,amarillo,azul,morado]
#pantallaTamaño
patata=(600,600)
patata1=(600,800)
patata2=(800,600)

verdulero=[patata,patata1,patata2]
pygame.init()
amarillo=pygame.Color(255,255,0)#esta esta opcion para crear colores//COLOR VA CON MAYUSCULAS
pantalla= pygame.display.set_mode(patata)#ANCHO ALTO DE LA PANTALLA
pygame.display.set_caption("JUEGITO")#TITULO
#controlador de FPS
clock=pygame.time.Clock()

#cordenadas
cordX=90
cordY=250
#velocidad
velocidadX=6
velocidadY=6
#cordenadasVariables
i=0
pygame.draw.line(pantalla,azul,(80,60),(200,300))
while True:#EL JUEGO VA A CORRER MIENTRAS WHILE SEA IGUAL A true
    #colisiones
    if (cordX<0 or cordX>520):
        velocidadX*=-1
        pantalla= pygame.display.set_mode(patata2)
        amarillo=rojo
        print("cambio")
        i+=1

    if (cordY>620 or cordY<0):
        pantalla= pygame.display.set_mode(patata1)
        amarillo=azul
        velocidadY*=-1
        i+=1
    cordX+=velocidadX
    cordY+=velocidadY

    #for i in range(5):#se pueden iterar las imagenes de fondo si lo pones una lista
    #    pygame.draw.line(pantalla,azul,(80,60+i*5),(200,300+i*5),55)
    #    pantalla.fill(amarillo)#hay que pasarle una variable con el codigo del color // la opcion fill es para el fondo
    for evento in pygame.event.get():#este for each lo que hace es asignarle el evento a "evento"
        if evento.type == QUIT:#posteriormente el evento va a ser evaludo de diferentes formas adentro del for
            pygame.quit()#                      ||
            sys.exit()#                         ||
    #fondo
    amarillo=amarillo
    pantalla.fill(amarillo)
    if (i==5):
        i=0
    pygame.draw.rect(pantalla, lista[i], (cordX,cordY, 80,80))

    pygame.display.flip()#actualizar ventana TODAVIA NO SE QUE HACE
    clock.tick(60)
