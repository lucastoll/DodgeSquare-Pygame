import pygame
from pygame.locals import * #Importa todas as funções e constantes.
from sys import exit
from time import sleep
from random import randint
controle =1

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
xlinha = -1
xlinha2 = 1023
xlinha3 = -1
xlinha4 = -1

ylinha = 0
ylinha2 = 0
ylinha3 = 0
#Controle retângulo player.
xrec = 492
yrec = 384
#Controle retângulo pontuação.ds
xpontos = 492
ypontos = 184
pontos = 1

xlinhuda=0
ylinhuda=1
ylinhuda2=altura

timer=6000

while True:
    clock.tick(300)  # FPS
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
    player = pygame.draw.rect(tela, (0, 0, 255), (xrec, yrec, 40, 40))  # TELA (RGB) (X, Y, LARGURA, ALTURA)
    ponto = pygame.draw.rect(tela, (250, 253, 15), (xpontos, ypontos, 10, 10))

    #Teste retorno circulo e linha
    if ycirc >= altura:  # Circulo volta ao topo da janela quando ultrapa ssa o limite baixo (altura)
        ycirc = 0
    ycirc += 1  # Cada vez que atualiza o loop o circulo desce um pixel

    #Colisão player x linha
    if xlinha >= largura:  # Linha volta ao começo da tela quando chega ao limite (largura)
        xlinha = 0
    if xlinha2 <= 0:  # Linha volta ao começo da tela quando chega ao limite (largura)
        xlinha2 = 1023
    if xlinha3 >= largura:  # Linha volta ao começo da tela quando chega ao limite (largura)
        xlinha3 = 0
    if xlinha4 >= largura:  # Linha volta ao começo da tela quando chega ao limite (largura)
        xlinha4 = 0
    timer+=1
    #Linha esquerda para direita
    if timer > 1000:
        linha1 = pygame.draw.rect(tela, (0, 255, 0), (xlinha, ylinha, 5, altura))
        xlinha+=0.6
        if player.colliderect(linha1):
            pontos -= 1
            xlinha=-500
    #Linha direita para esquerda
    if timer > 2500:
        linha2 = pygame.draw.rect(tela, (0, 255, 0), (xlinha2, ylinha, 5, altura))
        xlinha2-=0.6
        if player.colliderect(linha2):
            pontos -= 1
            xlinha2=1500
    #Linha cima para baixo
    if timer > 4000:
        linhuda = pygame.draw.line(tela, (0, 255, 0), [0, ylinhuda], [1024, ylinhuda], 5)
        ylinhuda += 0.5
        for c in range(0, 21):
            c * 0, 1
            if ylinhuda - c == yrec:
                pontos -= 1
                ylinhuda = -500
        for c in range(0, 6):
            c * 0, 1
            if ylinhuda + c == yrec:
                pontos -= 1
                ylinhuda = -500
        if ylinhuda >= altura:  # Linha volta ao começo da tela quando chega ao limite (largura)
            ylinhuda = 0
    #Linha baixo para cima
    if timer > 6000:
        linhuda2 = pygame.draw.line(tela, (0, 255, 0), [0, ylinhuda2], [1024, ylinhuda2], 5)
        ylinhuda2 -= 0.5
        for s in range(0, 21):
            s * 0, 1
            if ylinhuda2 - s == yrec:
                pontos -= 1
                ylinhuda2 = 1000
        for s in range(0, 6):
            s * 0, 1
            if ylinhuda2 + s == yrec:
                pontos -= 1
                ylinhuda2 = 1000
        if ylinhuda2 <= 0:  # Linha volta ao começo da tela quando chega ao limite (largura)
            ylinhuda2 = 1000



    #Colisão player x ponto
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
    mensagem2 = f'xrec: {xrec}' #Pontuação mensagem
    texto_formatado2 = fonte.render(mensagem2, True, (255, 255, 255)) #Renderizar o texto
    tela.blit(texto_formatado2, (largura - 500, 1))