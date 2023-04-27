import pygame
from sys import exit

pygame.init()
surface = pygame.display.set_mode((400,300))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    color = (0,255,0)

    pygame.draw.rect(surface, color, pygame.Rect(30,30,60,60))
    pygame.display.flip()

    pygame.display.update()
    clock.tick(1)

