import pygame, sys
pygame.init()

#colores
blanco=(255,255,255)
negro=(0,0,0)
rojo=(255,0,0)
#tamaño de la pantalla
tam=(800,600)
#pantalla y velocidad
pantalla=pygame.display.set_mode(tam)
clock=pygame.time.Clock()
#condicion del while
game_over=False
#PALETA IZQUIERDA
cordenada_x_i=50
cordenada_y_i=255
velocidad_y_i=0
velocidad_x_i=0
#PALERA DERECHA
cordenada_x_d=750
cordenada_y_d=255
velocidad_y_d=0
velocidad_x_d=0
#pelota
cordenada_x_p=400
cordenada_y_p=300
velocidad_x_p=1
velcoidad_y_p=3
#juego
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        #PALETA DE LA IZQUIERDA
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                velocidad_y_i=-6
            if event.key==pygame.K_s:
                velocidad_y_i=6
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_s:
                velocidad_y_i=0
            if event.key==pygame.K_w:
                velocidad_y_i=0
        #PALETA DE LA DERECHA
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                velocidad_y_d=-6
            if event.key==pygame.K_DOWN:
                velocidad_y_d=6
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                velocidad_y_d=0
            if event.key==pygame.K_DOWN:
                velocidad_y_d=0

    cordenada_y_p+=velcoidad_y_p
    if cordenada_y_p>590 or cordenada_y_p<0:
        velcoidad_y_p*=-1



    pantalla.fill(negro)
    #zona de dibujo
    cordenada_y_i+=velocidad_y_i
    cordenada_y_d+=velocidad_y_d


    pygame.draw.circle(pantalla, blanco,(cordenada_x_p,cordenada_y_p),10)
    pygame.draw.rect(pantalla, blanco, (cordenada_x_i,cordenada_y_i,15,90))
    pygame.draw.rect(pantalla, blanco, (cordenada_x_d,cordenada_y_d,15,90))

    pygame.display.flip()
    clock.tick(60)
