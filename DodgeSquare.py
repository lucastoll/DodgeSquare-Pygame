import pygame
from pygame.locals import * #Importa todas as funções e constantes.
from sys import exit
from time import sleep
from random import randint
#Dimensões tela
largura = 1024  # Eixo X
altura = 768  # Eixo Y

#Iniciliazações
pygame.init  # Iniciliza o pygame, precisa do parentêses para iniciar a fonte.
pygame.font.init() #Inicializa a fonte.
fonte = pygame.font.SysFont('arial', 40, True, True)  # Inicializar fonte
clock = pygame.time.Clock()  # Iniciliazar FPS
tela = pygame.display.set_mode((largura, altura))  # Criação da Janela do game
pygame.display.set_caption('Jogo')  # Nome da janela do jogo

#Controle circulo teste
xcirc = 512
ycirc = 0
#Controle linha teste
xlinha = 0
ylinha = 0
#Controle retângulo player.
xrec = 492
yrec = 384
#Controle retângulo pontuação.
xpontos = 492
ypontos = 184
pontos = 0

while True:
    clock.tick(500)  # FPS
    mensagem = f'Pontos: {pontos}' #Pontuação mensagem
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255)) #Renderizar o texto

    for event in pygame.event.get():  # Loop verficação de ação, para fechar o programa quando pedido.
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:  # Movimentação quadrado com setas
            if event.key == K_LEFT:
                xrec -= 100
            if event.key == K_UP:
                yrec -= 100
            if event.key == K_DOWN:
                yrec += 100
            if event.key == K_RIGHT:
                xrec += 100

    pygame.display.update()  # Comando necessário pro jogo rodar, se não usar isso ele só roda um frame
    tela.fill((0, 0, 0))  # Se não colocar isso os objetos se movem porém o rastro fica todo pintado.

    # OBJETOS NA TELA
    pygame.draw.circle(tela, (230, 0, 0), (xcirc, ycirc), 10)  # TELA (RGB) (X,Y) RAIO
    player = pygame.draw.rect(tela, (0, 0, 255), (xrec, yrec, 40, 40))  # TELA (RGB) (X, Y, LARGURA, ALTURA)
    ponto = pygame.draw.rect(tela, (250, 253, 15), (xpontos, ypontos, 10, 10))
    pygame.draw.line(tela, (0, 255, 0), [xlinha, 0], [xlinha, altura], 10)

    if ycirc >= altura:  # Circulo volta ao topo da janela quando ultrapa ssa o limite baixo (altura)
        ycirc = 0
    ycirc += 1  # Cada vez que atualiza o loop o circulo desce um pixel

    if xlinha >= largura:  # Linha volta ao começo da tela quando chega ao limite (largura)
        xlinha = 0
    xlinha += 1
    #
    if player.colliderect(ponto):
        pontos += 1
        xpontos = randint(24, 924)
        ypontos = randint(100, 668)

    # Movimentação quadrado com wasd pressionando

    if pygame.key.get_pressed()[K_a]:
        xrec -= 1
    if pygame.key.get_pressed()[K_w]:
        yrec -= 1
    if pygame.key.get_pressed()[K_s]:
        yrec += 1
    if pygame.key.get_pressed()[K_d]:
        xrec += 1

    # Código para o quadrado não ultrapassar a tela

    if yrec <= 0:  # 768
        yrec += altura
    if xrec <= 0:  # 768
        xrec += largura
    if xrec >= largura:  # 1024
        xrec = 0
    if yrec >= altura:  # 768
        yrec = 0

    # printar texto
    tela.blit(texto_formatado, (largura - 250, 1))