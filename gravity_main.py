import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((400,400))
    pygame.display.set_caption("gravity")

    fps = 100
    fpsClock = pygame.time.Clock()

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    ball = pygame.image.load("ball.png")
    x = 175
    h = 50
    t=0
    t_v=0
    v=0
    #g=1.625 #moon g value
    g=9.8
    yon = "down"




    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.blit(background, (0, 0))
        h,t,v,yon,t_v=gravity(h,t,yon,v,g,t_v)
        screen.blit(ball, (x, h))
        pygame.display.flip()
        pygame.display.update()
        fpsClock.tick(fps)

def gravity(h,t,yon,v,g,t_v):
    zaman=0.01
    t   += zaman #her refresh 0.01ms
    t_v += zaman

    if yon =="down":

        if h < 375:
            v += (g * t)
            h += (v*0.01 + g*t**2)/2

            print("v_down: ",v)
        if h >= 375:
            yon = "up"
            t=0


    if yon =="up":
        if v >= 0:
            v -= (g * t_v)

            h -= (v*0.01-(g*t**2)/2)

            print("v_up: ",v)
        if v < 0:
            yon = "down"
            t_v = 0




    return h,t,v,yon,t_v


main()
