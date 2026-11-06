#Iniciar jogo da cobrinha projeto estudo
#Pygame não esta sendo reconhecido 

import pygame
from pygame.locals import * 

# Configurações da janela do jogo
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
POS_INICIAL_X = WINDOW_WIDTH // 2
POS_INICIAL_Y = WINDOW_HEIGHT // 2
BLOCK_SIZE = 10

pygame.init() # Inicia o módulo pygame
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Configurações da cobra
cobra_pos = [(POS_INICIAL_X, POS_INICIAL_Y)]
cobra_surface = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
cobra_surface.fill((54, 60, 74))

# Loop principal do jogo
while True: 
    window.fill((68,189,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    for pos in cobra_pos:
        window.blit(cobra_surface, pos) # Usando o método blit para desenhar a cobra na tela

    # Atualiza a tela do jogo
    pygame.display.update()