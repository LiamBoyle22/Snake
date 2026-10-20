import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()

surface1 = pygame.Surface((100,200))
surface1.fill((0,0,225))

while True: #main game loop

    #quit window event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70))
    screen.blit(surface1, (200,250))
    pygame.display.update()
    clock.tick(60)