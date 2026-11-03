#Iniciar jogo da cobrinha projeto estudo

import pygame
from pygame.locals import *


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

while True:
    window.fill((68,189,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()