import pygame
import sys

pygame.init()

LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("jogo de movimento de colisão")

AZUL = (0,120,255)
VERDE = (0,255,0)
VERMELHO = (255,0,0)

#JOGADOR PLAYER

jogador = pygame.Rect(100,300,50,50)

#OBSTACULO

obstaculo = pygame.Rect(500,300,50,50)

#velocidade do jogador

velocidade  = 5

#adicionando vidas

vidas = 3

#Adição controlar colisao

colidindo = False

# Clock para controlar fps
clock = pygame.time.Clock()

#teclas precionadas



tela.fill(AZUL)
pygame.draw.rect(tela,VERDE,jogador)
pygame.draw.rect(tela,VERMELHO,obstaculo)
pygame.display.flip()

#LOOP PRINCIPAL

while (True):
    for evento in pygame.event.get():
        if(evento.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

    teclas  = pygame.key.get_pressed()

#salva a ultina posição quando colidir
    jogador_anterior  = jogador.copy()


    if teclas[pygame.K_UP]:
        jogador.y -=velocidade
    if teclas[pygame.K_DOWN]:
        jogador.y += velocidade
    if teclas [pygame.K_LEFT]:
        jogador.x -= velocidade
    if teclas [pygame.K_RIGHT]:
        jogador.x += velocidade


    jogador.x = max(0, min(jogador.x, LARGURA - jogador.width))
    jogador.y = max(0, min(jogador.y, ALTURA - jogador.height))

    if jogador.colliderect(obstaculo):
        if not colidindo:
            vidas -=1
            print(f"Colisão detectada! vidas restantes{vidas}")
            colidindo = True

            #Verificando game over

            if vidas <= 0:
                print("GAME OVER!!!")
                pygame.quit()
                sys.exit()

        jogador = jogador_anterior
    else:
        colidindo = False            

        print("colisão detectada")


#rederização

    tela.fill(AZUL)
    pygame.draw.rect(tela, VERDE, jogador)       
    pygame.draw.rect(tela,VERMELHO,obstaculo)
    
    fonte = pygame.font.SysFont(None,36)
    texto_vidas = fonte.render(f"vidas, {vidas}", True, (255,255,255))
    tela.blit(texto_vidas,(10,10))
   
    pygame.display.flip()


    clock.tick(60)  

