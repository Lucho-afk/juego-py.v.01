import pygame, sys, random
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
velocidad_x_p=random.choice([-3,3])
velocidad_y_p=random.choice([-3,3])
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
                if cordenada_y_i>0:

                    velocidad_y_d=-6
            if event.key==pygame.K_DOWN and cordenada_y_i<510:

                    velocidad_y_d=6
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                velocidad_y_d=0
            if event.key==pygame.K_DOWN:
                velocidad_y_d=0
    #esto es pa que no se vaya por arriba y vuelva al centro por los costados
    cordenada_y_p+=velocidad_y_p
    cordenada_x_p+=velocidad_x_p
    if cordenada_y_p>590 or cordenada_y_p<0:
        velocidad_y_p*=-1
    if cordenada_x_p>830 or cordenada_x_p<-30:
        cordenada_x_p=400
        cordenada_y_p=300
        velocidad_x_p*=random.choice([1,-1])
        velocidad_y_p*=random.choice([1,-1])

    pantalla.fill(negro)
    #zona de dibujo
    cordenada_y_i+=velocidad_y_i
    cordenada_y_d+=velocidad_y_d


    pelota=pygame.draw.circle(pantalla, blanco,(cordenada_x_p,cordenada_y_p),10)
    jugador1=pygame.draw.rect(pantalla, blanco, (cordenada_x_i,cordenada_y_i,15,90))
    jugador2=pygame.draw.rect(pantalla, blanco, (cordenada_x_d,cordenada_y_d,15,90))

    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        velocidad_x_p*=-1
        velocidad_y_p*=random.choice([1,-1])

    pygame.display.flip()
    clock.tick(60)
