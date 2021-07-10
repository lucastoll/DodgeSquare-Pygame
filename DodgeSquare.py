import pygame
from pygame.locals import * #Importa todas as funções e constantes.
from sys import exit
from time import sleep
from random import randint

#Funções
def colisao(): #Função colisão player x linhas
    global vidas
    damage_sound.play()
    sleep(1)
    vidas -= 1

def reiniciar(): #Função para reiniciar o jogo
    global xlinha, xlinha2, ylinha, timer, Vylinha, Vylinha2, xrec, yrec, xpontos, ypontos, dead, pontos, vidas
    pygame.mixer.music.play(-1)
    vidas = 3
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

#Variáveis
velocidade = 300 #FPS
vidas = 3 #Controle vidas
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
pygame.display.set_caption('DodgeSquare')  # Nome da janela do jogo
timer=0 #Contador de tempo do jogo

# Sons
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.load('content/xDeviruchi - Minigame .mp3') #Background music


damage_sound = pygame.mixer.Sound('content/smas_damage.wav')
heartup_sound = pygame.mixer.Sound('content/smas_heart.wav')
coin_sound = pygame.mixer.Sound('content/smw_coin.wav')
gameover_sound = pygame.mixer.Sound('content/smw_gameover.wav')
win_sound = pygame.mixer.Sound('content/smw_win.wav')

#Imagens
heart = pygame.image.load('content/heart.png')
heart = pygame.transform.scale(heart, (50, 50))

ganhou = pygame.image.load('content/ganhou.jpeg')
perdeu = pygame.image.load('content/perdeu.jpeg')
perdeu2 = pygame.image.load('content/perdeu2.jpeg')
perdeu2 = pygame.transform.scale(perdeu2, (500, 500))
recorde = pygame.image.load('content/recorde.jpeg')
recorde = pygame.transform.scale(recorde, (400, 400))
wrecord = pygame.image.load('content/wrecord.png')
setas = pygame.image.load('content/setas.jpg')
setas = pygame.transform.scale(setas, (200, 100))


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

start = True
while start:
    for event in pygame.event.get():  # Loop verficação de ação, para fechar o programa quando pedido.
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:  # Movimentação quadrado com setas
            if event.key == K_r:
                start = False
    pygame.draw.line(tela, (0, 255, 0), [0, 50], [1024, 50], 5)
    pygame.draw.rect(tela, (0, 255, 0), (950, 0, 5, altura))
    pygame.draw.rect(tela, (0, 0, 255), (850, 100, 40, 40))
    pygame.draw.rect(tela, (250, 253, 15), (800, 150, 10, 10))
    fonte_start = pygame.font.SysFont('Bahnschrift', 60, True)  # Inicializar fonte
    fonte_start2 = pygame.font.SysFont('Arial', 20, True)  # Inicializar fonte
    mensagem_start = 'DodgeSquare'
    mensagem_start2 = 'Como jogar:'
    mensagem_start3 = 'W'
    mensagem_start4 = 'ASD'
    mensagem_start5 = 'Move o quadrado'
    mensagem_start6 = 'Você controla o quadrado azul e precisa pegar o quadrado amarelo enquanto desvia das linhas'
    mensagem_start7 = 'Teleporta o quadrado'
    mensagem_start8 = 'Se o quadrado azul ultrapassar algum limite da tela ele aparece no limite contrário'
    mensagem_start9 = 'Você tem 3 vidas e precisa de 30 pontos para ganhar.'
    mensagem_start10 = 'Pressione R para começar'

    texto_start = fonte_start.render(mensagem_start, True, (255, 255, 255))
    texto_start2 = fonte_start2.render(mensagem_start6, True, (255, 255, 255))
    texto_start3 = fonte_start2.render(mensagem_start2, True, (255, 255, 255))
    texto_start4 = fonte_start.render(mensagem_start3, True, (255, 255, 255))
    texto_start5 = fonte_start.render(mensagem_start4, True, (255, 255, 255))
    texto_start6 = fonte_start2.render(mensagem_start5, True, (255, 255, 255))
    texto_start7 = fonte_start2.render(mensagem_start7, True, (255, 255, 255))
    texto_start8 = fonte_start2.render(mensagem_start8, True, (255, 255, 255))
    texto_start9 = fonte_start2.render(mensagem_start9, True, (255, 255, 255))
    texto_start10 = fonte_start2.render(mensagem_start10, True, (255, 255, 255))

    tela.blit(texto_start, (largura / 3.3, 100))
    tela.blit(texto_start2, (30, 200))
    tela.blit(texto_start3, (largura / 2 - 80, 240))
    tela.blit(texto_start4, (300, 300))
    tela.blit(texto_start5, (260, 350))
    tela.blit(texto_start6, (240, 420))
    tela.blit(setas, (600, 320))
    tela.blit(texto_start7, (600, 420))
    tela.blit(texto_start8, (100, 700))
    tela.blit(heart, (430, 500))
    tela.blit(heart, (480, 500))
    tela.blit(heart, (530, 500))
    tela.blit(texto_start9, (230, 550))
    tela.blit(texto_start10, (370, 600))

    pygame.display.update()  # Atualiza o display com os textos novos
pygame.mixer.music.play(-1)  # musica principal play forever
while True:
    if vidas == 3:
        tela.blit(heart, (0,0))
        tela.blit(heart, (50,0))
        tela.blit(heart, (100,0))
    elif vidas == 2:
        tela.blit(heart, (0,0))
        tela.blit(heart, (50,0))
    elif vidas == 1:
        tela.blit(heart, (0,0))

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
    if vidas == 0:
        pygame.mixer.music.fadeout(500)  #para a música depois de um tempinho
        tela.fill((0, 0, 0))
        fonte = pygame.font.SysFont('arial', 40, True)  # Inicializar fonte
        mensagem_loss = 'Você perdeu'
        mensagem_loss2 = 'Pressione R para jogar novamente'
        mensagem_win  = 'Você ganhou'
        mensagem_win2 = 'Recompensa = +2 QI'
        mensagem_win3 = 'Pressione R para jogar novamente'
        mensagem_record = 'RECORDE MUNDIAL!!!!!!!!!!!!!'

        texto_formatado = fonte.render(mensagem, True, (255, 255, 255))  # Renderizar o texto
        tela.blit(texto_formatado, (largura / 2 - 100, 1))
        texto_loss = fonte.render(mensagem_loss, True, (255, 255, 255)) #Texto dividido em partes pois o \n não funciona aqui.
        texto_loss2 = fonte.render(mensagem_loss2, True, (255, 255, 255))
        texto_win = fonte.render(mensagem_win, True, (255, 255, 255))
        texto_win2 = fonte.render(mensagem_win2, True, (255, 255, 255))
        texto_win3 = fonte.render(mensagem_win3, True, (255, 255, 255))
        texto_recorde = fonte.render(mensagem_record, True, (255, 255, 255))
        if (pontos >= 30) & (pontos < 50):
            win_sound.play()
            tela.blit(texto_win, (largura/2 - 130, 100))
            tela.blit(texto_win2, (largura/2 - 200, 200))
            tela.blit(texto_win3, (largura/2 - 320, 300))
            tela.blit(ganhou, ((largura/2 - 350, 400)))
        elif pontos >= 50:
            win_sound.play()
            tela.blit(texto_recorde, (largura / 2 - 250, 100))
            tela.blit(texto_win2, (largura / 2 - 200, 200))
            tela.blit(texto_win3, (largura / 2 - 320, 300))
            tela.blit(wrecord, ((largura / 2 - 350, 400)))
            tela.blit(recorde, ((largura / 2, 350)))
        else:
            gameover_sound.play()
            tela.blit(texto_loss, (largura / 2 - 120, 100))
            tela.blit(texto_loss2, (largura / 2 - 320, 200))
            perdeu_imagem = randint(1, 2)
            if perdeu_imagem == 1:
                tela.blit(perdeu, (largura / 2 - 300, 280))
            else:
                tela.blit(perdeu2, (largura / 2 - 240, 300))

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
    if (timer > 8000) & (timer < 12000):
        velocidade = 320
    elif (timer > 12000) & (timer < 16000):
        velocidade = 340
    elif (timer > 16000):
        velocidade = 360


    #Colisão player x ponto
    if player.colliderect(ponto):
        pontos += 1
        xpontos = randint(104, 924)
        ypontos = randint(100, 690)
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
    # mensagem2 = f'VE {velocidade} TI {timer}' #Pontuação mensagem
    # texto_formatado2 = fonte.render(mensagem2, True, (255, 255, 255)) #Renderizar o texto
    # tela.blit(texto_formatado2, (largura - 500, 100))