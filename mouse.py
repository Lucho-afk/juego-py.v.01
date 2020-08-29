import pygame, sys

pygame.init()

negro=(0,0,0)
violeta=(255,0,255)
blanco=(255,255,255)

tam=(600,600)
pantalla= pygame.display.set_mode(tam)
clock=pygame.time.Clock()
pygame.mouse.set_visible(0)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    pantalla.fill(blanco)
    mouse=pygame.mouse.get_pos()
    print(mouse)
    x=mouse[0]
    y=mouse[1]

    pygame.draw.circle(pantalla, violeta, (x,y), 10)
    pygame.display.flip()
    clock.tick(30)
