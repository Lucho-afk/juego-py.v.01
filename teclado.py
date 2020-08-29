import pygame, sys

pygame.init()

negro=(0,0,0)
violeta=(255,0,255)
blanco=(255,255,255)

tam=(600,600)
pantalla= pygame.display.set_mode(tam)
clock=pygame.time.Clock()

#CORDENADAS DEL CUADRADO
cord_x=300
cord_y=300
#velocidad
x_velocidad=0
y_velocidad=0

while True:
    for event in pygame.event.get():#ACA ESTAN LOS EVENTOS DEL juego
        if event.type==pygame.QUIT:
            sys.exit()
        #eventos del teclado, tiene que ir adentro del for de eventos porque sino no funca

        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_RIGHT:
                x_velocidad=3
            if event.key==pygame.K_LEFT:
                x_velocidad=-3
            if event.key==pygame.K_UP:
                y_velocidad=-3
            if event.key==pygame.K_DOWN:
                y_velocidad=3
            if event.key==pygame.K_h:
                x_velocidad*=3
                y_velocidad*=3
            if event.key==pygame.K_SPACE:
                pass


        if event.type==pygame.KEYUP:

            if event.key==pygame.K_RIGHT:
                x_velocidad=0
            if event.key==pygame.K_LEFT:
                x_velocidad=0
            if event.key==pygame.K_UP:
                y_velocidad=0
            if event.key==pygame.K_DOWN:
                y_velocidad=0
            if event.key==pygame.K_h:
                x_velocidad=0
                y_velocidad=0



    pantalla.fill(blanco)

    cord_x+=x_velocidad
    cord_y+=y_velocidad


    pygame.draw.circle(pantalla, violeta, (cord_x,cord_y), 10)


    pygame.display.flip()
    clock.tick(60)
