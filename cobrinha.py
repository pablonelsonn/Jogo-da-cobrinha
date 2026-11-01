#Iniciar jogo da cobrinha projeto estudo

import pygame
import pygame.locals 
import random 
import time 

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
BLOCK = 10

pygame.font.init()
fonte = pygame.font.SysFont('Arial', 35, True, True) # negrito italico, ambos true
