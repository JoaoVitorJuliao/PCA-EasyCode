import pygame
import Mensagem
import os, sys

from pygame.locals import *
from TabelaPeriodica import TabelaPeriodica
from Pergunta import Pergunta
from ranking import *
mainClock = pygame.time.Clock()

pygame.init()
windowWidth = 1140
windowHeight = 700
gameDisplay = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Periodic.Py')

tabela = TabelaPeriodica()
pergunta = Pergunta()

# CORES
gray = (246, 246, 246)
black = (0, 0, 0)
white = (255, 255, 255)
green = (75, 181, 67)

# POSICAO IMAGEM
posicaoTuboEnsaio = (500, 600)

# PONTUACAO
pontuacao = 0

vidas = 1
botao_jogarNovamente = Botao(cor=green, posx=310, posy=360, largura=180, altura=40, texto="Jogar Novamente")
botao_start = Botao(cor=black, posx=479, posy=250, largura=200, altura=40, texto='Iniciar Jogo')
botao_options = Botao(cor=black, posx=478, posy=300, largura=200, altura=40, texto='Opções do jogo')

# BOTAO NA JANELA DE OPÇOES
botao_voltar = Botao(cor=black, posx=0, posy=0, largura=100, altura=40, texto='Voltar')

pygame.font.init()

# FONTES PARA ESCRITA NA TELA
fonteTituloJogo = pygame.font.SysFont('comicsansms', 52)
fonteNomeDoJogador = pygame.font.SysFont('comicsansms', 24)
fontePontuacao = pygame.font.SysFont('comicsansms', 24)
fonteSugestao = pygame.font.SysFont('comicsansms', 24)
fonteElemento = pygame.font.SysFont('comicsansms', 20)
fonteBotaoConfirmar = pygame.font.SysFont('comicsansms', 24)
fonteMensagem = pygame.font.SysFont('comicsansms', 36)

tubo = pygame.image.load(os.path.join('resources', 'tubo1.png'))

gameExit = False
firstInit = True
listaElementosSelecionados = []
mostraMensagemTempo = 0
fimdejogo = False


def mostrarvidas():
    fonte = pygame.font.SysFont('comicsansms', 20)
    corrente = "Vidas: " + str(vidas).zfill(2)
    texto = fonte.render(corrente, True, black)
    texto_rect = texto.get_rect()
    texto_rect.topright = [100, 0]
    gameDisplay.blit(texto, texto_rect)


def verificaPontuacao(nome_jogador, pontuacao):
    atual = pontuacao
    nome = nome_jogador
    arq = open('HighScores.txt', 'r')
    lista = []
    lista2 = []
    for l in arq:
        lista = l.split(';')
    trocou = 0
    i = 0
    for pos in lista:
        i += 1
        quebra = pos.split(':')
        if trocou == 0 and int(quebra[1]) < atual:
            quebra[0] = nome
            quebra[1] = atual
            lista2.append(quebra[0]+":"+str(quebra[1]))
            trocou += 1
        else:
            lista2.append(quebra[0]+":"+str(quebra[1]))
    arq.close()
    i = 0
    arq = open('HighScores.txt', 'w')
    for pos in lista2:
        if i == 2:
            arq.write(pos)
        else:
            arq.write(pos+';')
        i += 1
    arq.close()


def mostraPontuacao():
    arq = open('HighScores.txt', 'r')
    for l in arq:
        lista = l.split(';')
        exibe_rk = fonteMensagem.render("RANKING", True, (25, 25, 112))
        exibe_p1 = fonteMensagem.render((f"1º lugar----> "+lista[0]), True, (25, 25, 112))
    # exibe_p2 = fonteMensagem.render(("2º lugar----> "+lista[1]), True, (25, 25, 112))
    # exibe_p3 = fonteMensagem.render(("3º lugar----> "+lista[2]), True, (25, 25, 112))
        gameDisplay.blit(exibe_rk, (352.5, 190))
        gameDisplay.blit(exibe_p1, (288, 230))
    # gameDisplay.blit(exibe_p2, (288, 260))
    # gameDisplay.blit(exibe_p3, (288, 290))


def main_menu():
    while True:

        gameDisplay.fill(white)

        botao_start.desenhaBotao(gameDisplay, white)
        botao_options.desenhaBotao(gameDisplay, green)

        for event in pygame.event.get():
            pos_mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_start.mouseSobre(pos_mouse):
                    game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_options.mouseSobre(pos_mouse):
                    options()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            # if event.type == MOUSEBUTTONDOWN:
            #     if event.button == 1:
            #         click = True

        pygame.display.update()
        mainClock.tick(60)


def options():
    running = True
    while running:
        gameDisplay.fill(white)
        botao_voltar.desenhaBotao(gameDisplay, white)
        for event in pygame.event.get():
            pos_mouse = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.mouseSobre(pos_mouse):
                    main_menu()

        pygame.display.update()
        mainClock.tick(60)


def game():
    firstInit = True
    listaElementosSelecionados = []
    mostraMensagemTempo = 0
    pontuacao = 0
    vidas = 1
    gameExit = False
    while not gameExit:
        gameDisplay.fill(gray)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                posicaoMouse = pygame.mouse.get_pos()
                if posicaoMouse[0] >= 950 and posicaoMouse[0] <= 950 + 150 and posicaoMouse[1] >= 638 and posicaoMouse[1] <= 638 + 50:
                    del elementoSelecionado
                    if pergunta.checarResposta(listaElementosSelecionados):
                        mostraMensagem = True
                        mensagem = 'Parabéns! Você Acertou!'

                        pontuacao = pontuacao + 1

                        pergunta.novaPergunta()

                        del listaElementosSelecionados[:]
                        del ultimoElementoInserido
                    else:
                        mostraMensagem = True
                        mensagem = 'Opa! Tente Novamente!'

                        del listaElementosSelecionados[:]
                        del ultimoElementoInserido

                        vidas -= 1

                    if vidas <= 0:
                        verificaPontuacao(nome, int(pontuacao))
                        fimdejogo = True
                        while fimdejogo:
                            gameDisplay.fill(white)
                            for event in pygame.event.get():
                                pos_mouse = pygame.mouse.get_pos()
                                if event.type == pygame.QUIT:
                                    sys.exit()

                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if botao_jogarNovamente.mouseSobre(pos_mouse):
                                        fimdejogo = False
                                        main_menu()
                                        vidas = 3
                                        pontuacao = 0
                            # exibe_fim3 = fonteMensagem.render(nome, True, (green))
                            exibe_fim1 = fonteTituloJogo.render("Fim de Jogo!", True, (233, 233, 233))
                            exibe_fim2 = fonteMensagem.render(
                                ("Jogador: " + nome + "          Pontos obtidos:" + str(pontuacao)), True,
                                (233, 233, 233))
                            gameDisplay.blit(exibe_fim1, (280, 30))
                            gameDisplay.blit(exibe_fim2, (196, 120))
                            mostraPontuacao()
                            botao_jogarNovamente.desenhaBotao(gameDisplay, white)

                            pygame.display.flip()

                else:
                    elementoSelecionado = tabela.elementoClick(posicaoMouse[0], posicaoMouse[1])

            if event.type == pygame.MOUSEBUTTONUP:
                posicaoMouse = pygame.mouse.get_pos()
                if posicaoMouse[0] >= posicaoTuboEnsaio[0] and posicaoMouse[0] <= posicaoTuboEnsaio[0] + 115 and posicaoMouse[1] >= posicaoTuboEnsaio[1] and posicaoMouse[1] <= posicaoTuboEnsaio[1] + 115:
                    try:
                        if elementoSelecionado.nomeElemento != '':
                            listaElementosSelecionados.append(elementoSelecionado)
                            ultimoElementoInserido = elementoSelecionado
                    except:
                        pass
                        # print('Elemento não definido')

        if firstInit == True:
            # TITULO DO JOGO
            gameDisplay.blit(fonteTituloJogo.render("Periodic.Py", 1, black), (440, 20))
            gameDisplay.blit(fonteTituloJogo.render("Digite seu nome", 1, black), (440, 250))
            nome = Mensagem.ask(gameDisplay, '')
            if nome:
                pergunta.novaPergunta()
                firstInit = False
        else:
            # TITULO DO JOGO
            gameDisplay.blit(fonteTituloJogo.render("Periodic.Py", 1, black), (440, 20))

            # mostrar vidas
            mostrarvidas()

            # SAUDAÇÃO
            gameDisplay.blit(fonteNomeDoJogador.render('Jogador: ' + nome, 1, black), (460, 150))

            # PONTUACAO
            gameDisplay.blit(fontePontuacao.render('Pontuação: ' + str(int(pontuacao)), 1, black), (900, 5))

            # TUBO DE ENSAIO
            gameDisplay.blit(pygame.transform.scale(tubo, (115, 115)), posicaoTuboEnsaio)

            # ELEMENTO A SER ADVINHADO
            gameDisplay.blit(fonteSugestao.render('Elemento:', 1, black), (680, 600))
            gameDisplay.blit(fonteElemento.render(pergunta.nomeCompostoQuimico, 1, black), (705, 632))

            # MONTA TABELA PERIODICA
            tabela.desenhaTabelaPeriodica(gameDisplay)

            # DESENHA BOTAO
            if len(listaElementosSelecionados) > 0:
                pygame.draw.rect(gameDisplay, green, [950, 632, 150, 50])
                gameDisplay.blit(fonteBotaoConfirmar.render('Confirmar', 1, white), (970, 638))

            # DRAG AND DROP
            botaoMouse = pygame.mouse.get_pressed()
            try:
                if botaoMouse[0] == 1:
                    posicaoMouseDrag = pygame.mouse.get_pos()
                    elementoSelecionado.desenhaElemento(gameDisplay, posicaoMouseDrag[0] - (elementoSelecionado.base / 2), posicaoMouseDrag[1] - (elementoSelecionado.altura / 2))
            except:
                pass
                # print('Elemento nao definido')

            # DESENHA ULTIMO ELEMENTO INSERIDO
            try:
                ultimoElementoInserido.desenhaElemento(gameDisplay, 400, 610)
                gameDisplay.blit(fonteElemento.render('Último Inserido', 1, black), (360, 570))
            except:
                pass
                # print('Nao existe ultimo elemento')

            # MOSTRA MENSAGEM
            try:
                if mostraMensagem:
                    gameDisplay.blit(fonteMensagem.render(mensagem, 1, black), (240, 200))
                    mostraMensagemTempo = mostraMensagemTempo + 1
                    if mostraMensagemTempo > 100:
                        mostraMensagem = False
                        mostraMensagemTempo = 0

            except:
                pass
                # print('Mensagem nao definida')

            # REFRESH NA TELA
            pygame.time.wait(40)
            pygame.display.update()
main_menu()

pygame.display.update()
pygame.quit()

quit()
