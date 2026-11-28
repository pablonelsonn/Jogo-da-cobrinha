#Iniciar jogo da cobrinha projeto estudo
#Pygame não esta sendo reconhecido 

import pygame
from pygame.locals import * # pyright: ignore[reportWildcardImportFromLibrary]
import random

# Configurações da janela do jogo
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
POS_INICIAL_X = WINDOW_WIDTH // 2
POS_INICIAL_Y = WINDOW_HEIGHT // 2
BLOCK_SIZE = 10

def colisao(pos1, pos2):
     return pos1 == pos2

def verifica_margens(pos):
    if 0 <= pos[0] < WINDOW_WIDTH and 0 <= pos[1] < WINDOW_HEIGHT:
        return False
    else:
        return True

def gera_pos_aleatoria():
    x = random.randint(0, WINDOW_WIDTH )
    y = random.randint(0,  WINDOW_HEIGHT ) 
    return x // BLOCK_SIZE * BLOCK_SIZE, y // BLOCK_SIZE * BLOCK_SIZE

def gamer_Over():
    print("Game Over!")
    pygame.quit()
    quit()


pygame.init() # Inicia o módulo pygame
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Configurações da cobra
cobra_pos = [(POS_INICIAL_X, POS_INICIAL_Y)]
cobra_surface = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
cobra_surface.fill((54, 60, 74))
direcao = K_LEFT

maca_surface = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
maca_surface.fill((255, 0, 0))
maca_pos = gera_pos_aleatoria() # Gera uma posição aleatória para a maçã

# Loop principal do jogo
while True: 
    pygame.time.Clock().tick(10)
    window.fill((68,189,50))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif evento.type == pygame.KEYDOWN:
            if evento.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                direcao = evento.key

        if verifica_margens(cobra_pos[0]): # Verifica se a cobra saiu da tela
                 gamer_Over() # Chama a função de game over


    window.blit(maca_surface, maca_pos) # Desenha a maçã na tela
    # Desenha a cobra na tela e faz ela se mover de acordo com a direção

    if (colisao(cobra_pos[0], maca_pos)): # Verifica se a cobra colidiu com a maçã
         maca_pos = gera_pos_aleatoria() # Gera uma nova posição aleatória para a maçã

    for pos in cobra_pos:
        window.blit(cobra_surface, pos) # Usando o método blit para desenhar a cobra na tela

    # Atualiza a posição para a direita
        if direcao == K_RIGHT:
             cobra_pos[0] = (cobra_pos[0][0] + BLOCK_SIZE, cobra_pos[0][1]) #Movimenta a cobra para a direita

    # Atualiza a posição para a esquerda
        elif direcao == K_LEFT:
             cobra_pos[0] = (cobra_pos[0][0] - BLOCK_SIZE, cobra_pos[0][1]) #Movimenta a cobra para a esquerda
   
    # Atualiza a posição para cima
        elif direcao == K_UP:
             cobra_pos[0] = (cobra_pos[0][0], cobra_pos[0][1] - BLOCK_SIZE) #Movimenta a cobra para cima

    # Atualiza a posição para baixo
        elif direcao == K_DOWN:
            cobra_pos[0] = (cobra_pos[0][0], cobra_pos[0][1] + BLOCK_SIZE) #Movimenta a cobra para baixo

    #cobra_pos[0] = cobra_pos[0][0] + BLOCK_SIZE, cobra_pos[0][1] #Movimenta a cobra para a direita
    #cobra_pos[0] = cobra_pos[0][0] - BLOCK_SIZE, cobra_pos[0][1] #Movimenta a cobra para a esqueda
    #cobra_pos[0] = cobra_pos[0][0], cobra_pos[0][1] - BLOCK_SIZE #Movimenta a cobra para a cima
    #cobra_pos[0] = cobra_pos[0][0], cobra_pos[0][1] + BLOCK_SIZE #Movimenta a cobra para a baixo


    # Atualiza a tela do jogo
    pygame.display.update()