import pygame
from pygame.locals import * #Importa todas as funções e constantes.
from sys import exit
from time import sleep
from random import randint

#Funções
def colisao(): #Função colisão player x linhas
    global pontos
    damage_sound.play()
    sleep(1)
    pontos -= 1

def reiniciar(): #Função para reiniciar o jogo
    global xlinha, xlinha2, ylinha, timer, Vylinha, Vylinha2, xrec, yrec, xpontos, ypontos, dead, pontos
    pygame.mixer.music.play(-1)
    pontos = 0
    xlinha = -1
    xlinha2 = 1023
    ylinha = 0
    timer = 0
    Vylinha = 1
    Vylinha2 = altura
    xrec = 492
    yrec = 384
    xpontos = 492  # Um pouco acima do player para ele entender como funciona
    ypontos = 184
    dead = False

pontos = 0 #Precisa ser declarado depois da função.
win = 0 #Controle mensagem pos gameover

#Dimensões tela
largura = 1024  # Eixo X
altura = 768  # Eixo Y

#Iniciliazações
pygame.init()  # Iniciliza o pygame, precisa do parentêses para iniciar a fonte.
pygame.font.init() #Inicializa a fonte.
fonte = pygame.font.SysFont('arial', 40, True, True)  # Inicializar fonte
clock = pygame.time.Clock()  # Iniciliazar FPS
tela = pygame.display.set_mode((largura, altura))  # Criação da Janela do game
pygame.display.set_caption('Jogo')  # Nome da janela do jogo
timer=8000 #Contador de tempo do jogo

# Sons
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.load('xDeviruchi - Minigame .mp3') #Background music
pygame.mixer.music.play(-1)#musica principal play forever

damage_sound = pygame.mixer.Sound('smas_damage.wav')
heartup_sound = pygame.mixer.Sound('smas_heart.wav')
coin_sound = pygame.mixer.Sound('smw_coin.wav')
gameover_sound = pygame.mixer.Sound('smw_gameover.wav')
win_sound = pygame.mixer.Sound('smw_win.wav')

#Controle linhas horizontais
xlinha = -1
xlinha2 = 1023
ylinha = 0
#Controle linhas verticais
Vylinha=1
Vylinha2=altura
#Controle retângulo player.
xrec = 492
yrec = 384
#Controle retângulo pontuação.ds
xpontos = 492 #Um pouco acima do player para ele entender como funciona
ypontos = 184

velocidade = 300
while True:
    clock.tick(velocidade)  #FPS
    timer += 1 #Variavel contadora, usada para controlar o programa todo
    #Texto pontos
    mensagem = 'Pontos: {}'.format(pontos) #Pontuação mensagem
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255)) #Renderizar o texto
    tela.blit(texto_formatado, (largura - 250, 1))
    #Verificação ações
    for event in pygame.event.get():  # Loop verficação de ação, neccesário para verificar o contato com o teclado e se o usuario quer fechar o programa.
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:  # Movimentação quadrado com setas
            if event.key == K_LEFT:
                xrec -= 150
            if event.key == K_UP:
                yrec -= 150
            if event.key == K_DOWN:
                yrec += 150
            if event.key == K_RIGHT:
                xrec += 150
    #Gameover
    if pontos < 0:
        pygame.mixer.music.fadeout(500)  #para a música depois de um tempinho
        tela.fill((0, 0, 0))
        fonte = pygame.font.SysFont('arial', 40, True)  # Inicializar fonte
        mensagem_loss = 'Você perdeu'
        mensagem_loss2 = 'Pressione R para jogar novamente'
        mensagem_win  = 'Você ganhou'
        mensagem_win2 = 'Recompensa = +2 QI'
        mensagem_win3 = 'Pressione R para jogar novamente'

        texto_formatado = fonte.render(mensagem, True, (255, 255, 255))  # Renderizar o texto
        tela.blit(texto_formatado, (largura / 2 - 100, 1))
        texto_loss = fonte.render(mensagem_loss, True, (255, 255, 255)) #Texto dividido em partes pois o \n não funciona aqui.
        texto_loss2 = fonte.render(mensagem_loss2, True, (255, 255, 255))
        texto_win = fonte.render(mensagem_win, True, (255, 255, 255))
        texto_win2 = fonte.render(mensagem_win2, True, (255, 255, 255))
        texto_win3 = fonte.render(mensagem_win3, True, (255, 255, 255))
        if win == 1:
            win_sound.play()
            tela.blit(texto_win, (largura/2 - 130, 100))
            tela.blit(texto_win2, (largura/2 - 200, 200))
            tela.blit(texto_win3, (largura/2 - 320, 300))
        else:
            gameover_sound.play()
            tela.blit(texto_loss, (largura / 2 - 120, 100))
            tela.blit(texto_loss2, (largura / 2 - 320, 200))
        dead = True
        while dead: #while dead == True
            for event in pygame.event.get():  # Loop verficação de ação, para fechar o programa quando pedido.
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar()
            pygame.display.update() #Atualiza o display com os textos novos
    #fim gameover
    pygame.display.update()  #Comando necessário pro jogo rodar, se não usar isso ele só roda um frame
    tela.fill((0, 0, 0))  #Se não colocar isso os objetos se movem porém o rastro fica todo pintado.
    # OBJETOS NA TELA
    player = pygame.draw.rect(tela, (0, 0, 255), (xrec, yrec, 40, 40))  # TELA (RGB) (X, Y, LARGURA, ALTURA)
    ponto = pygame.draw.rect(tela, (250, 253, 15), (xpontos, ypontos, 10, 10))

    #Colisão player x linhas
    # #Linha esquerda para direita
    if timer > 1000:
        linha1 = pygame.draw.rect(tela, (0, 255, 0), (xlinha, ylinha, 5, altura))
        xlinha+=0.6
        if player.colliderect(linha1):
            colisao()
            xlinha=-500
        if xlinha >= largura:  # Linha volta ao começo da tela quando chega ao limite (largura)
            xlinha = 0
    # #Linha direita para esquerda
    if timer > 2500:
        linha2 = pygame.draw.rect(tela, (0, 255, 0), (xlinha2, ylinha, 5, altura))
        xlinha2-=0.6
        if player.colliderect(linha2):
            colisao()
            xlinha2=1500
        if xlinha2 <= 0:  # Linha volta ao começo da tela quando chega ao limite (largura)
            xlinha2 = 1023
    # #Linha cima para baixo
    if timer > 4000:
        pygame.draw.line(tela, (0, 255, 0), [0, Vylinha], [1024, Vylinha], 5)
        Vylinha += 0.5
        for c in range(0, 21):
            if Vylinha - c == yrec:
                colisao()
                Vylinha = -500
        for c in range(0, 4):
            if Vylinha + c == yrec:
                colisao()
                Vylinha = -500
        if Vylinha >= altura:  # Linha volta ao começo da tela quando chega ao limite (largura)
            Vylinha = 0
    #Linha baixo para cima
    if timer > 6000:
        pygame.draw.line(tela, (0, 255, 0), [0, Vylinha2], [1024, Vylinha2], 5)
        Vylinha2 -= 0.5
        for s in range(0, 35):
            if Vylinha2 - s == yrec:
                colisao()
                Vylinha2 = 1000
        for s in range(0, 4):
            if Vylinha2 + s == yrec:
                colisao()
                Vylinha2 = 1000
        if Vylinha2 <= 0:  # Linha volta ao começo da tela quando chega ao limite (largura)
            Vylinha2 = 1000
    if timer > 8000:
        velocidade = 400

    #Colisão player x ponto
    if player.colliderect(ponto):
        pontos += 1
        xpontos = randint(24, 924)
        ypontos = randint(100, 668)
        coin_sound.play()
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
    # mensagem2 = f'xrec: {xrec}' #Pontuação mensagem
    # texto_formatado2 = fonte.render(mensagem2, True, (255, 255, 255)) #Renderizar o texto
    # tela.blit(texto_formatado2, (largura - 500, 1))