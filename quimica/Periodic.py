import pygame
import Mensagem
import os, sys

from pygame.locals import *
from TabelaPeriodica import TabelaPeriodica
from Pergunta import Pergunta
from botao import Botao
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

# BOTAO JANELA MOSTRAR RESULTADO
botao_jogarNovamente = Botao(cor=black, posx=310, posy=360, largura=180, altura=40, texto="Jogar Novamente")
botao_voltar_menu = Botao(cor=black, posx=500, posy=360, largura=180, altura=40, texto="Voltar Menu")

# BOTOES DA JANELA MENU
botao_start = Botao(cor=black, posx=479, posy=250, largura=200, altura=40, texto='Iniciar')
botao_elementos = Botao(cor=black, posx=479, posy=300, largura=200, altura=40, texto='Sobre')
botao_options = Botao(cor=black, posx=479, posy=350, largura=200, altura=40, texto='Configurações')
botao_sair = Botao(cor=black, posx=479, posy=400, largura=200, altura=40, texto='Sair')

# BOTOES DA JANELA DE OPÇOES
botao_voltar = Botao(cor=black, posx=480, posy=350, largura=200, altura=40, texto='Voltar')
botao_som = Botao(cor=black, posx=478, posy=300, largura=200, altura=40, texto='Música: Ligada')
# BOTAO RESPOSTA
botao_voltar_resposta = Botao(cor=black, posx=5, posy=5, largura=200, altura=40, texto='Voltar')
# INICIA MODULOS DO PYGAME
pygame.font.init()

# FONTES PARA ESCRITA NA TELA
fonteTituloJogo = pygame.font.SysFont('comicsansms', 52)
fonteNomeDoJogador = pygame.font.SysFont('comicsansms', 24)
fontePontuacao = pygame.font.SysFont('comicsansms', 24)
fonteSugestao = pygame.font.SysFont('comicsansms', 24)
fonteElemento = pygame.font.SysFont('comicsansms', 20)
fonteBotaoConfirmar = pygame.font.SysFont('comicsansms', 24)
fonteMensagem = pygame.font.SysFont('comicsansms', 36)

# PASSANDO IMAGENS PARA O GAME
tubo = pygame.image.load(os.path.join('resources', 'tubo.png'))
menu_simbolo1 = pygame.image.load(os.path.join('resources', 'menu_simbolo1.svg'))
menu_simbolo2 = pygame.image.load(os.path.join('resources', 'menu_simbolo2.svg'))
menu_simbolo3 = pygame.image.load(os.path.join('resources', 'menu_simbolo3.svg'))

# CONFIGURAÇÕES DE SOM


def verificaPontuacao(nome_jogador, pontuacao):
    atual = pontuacao
    nome = nome_jogador
    arq = open('HighScores.txt', 'r')
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
        exibe_p1 = fonteMensagem.render(("1º lugar----> "+lista[0]), True, (25, 25, 112))
        exibe_p2 = fonteMensagem.render(("2º lugar----> "+lista[1]), True, (25, 25, 112))
        gameDisplay.blit(exibe_rk, (352.5, 190))
        gameDisplay.blit(exibe_p1, (288, 230))
        gameDisplay.blit(exibe_p2, (288, 260))


def main_menu():
    while True:
        gameDisplay.fill(white)

        gameDisplay.blit(fonteTituloJogo.render("Periodic.Py", 1, black), (440, 20))

        gameDisplay.blit(menu_simbolo1, (200, 200))
        gameDisplay.blit(menu_simbolo2, (800, 350))
        gameDisplay.blit(menu_simbolo3, (100, 450))

        botao_start.desenhaBotao(gameDisplay, white)
        botao_options.desenhaBotao(gameDisplay, white)
        botao_sair.desenhaBotao(gameDisplay, white)
        botao_elementos.desenhaBotao(gameDisplay, white)

        for event in pygame.event.get():
            pos_mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_start.mouseSobre(pos_mouse):
                    game()
                if botao_options.mouseSobre(pos_mouse):
                    opcoes()
                if botao_sair.mouseSobre(pos_mouse):
                    sys.exit()
                if botao_elementos.mouseSobre(pos_mouse):
                    respostas()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        mainClock.tick(60)


def opcoes():
    running = True
    while running:
        for event in pygame.event.get():
            pos_mouse = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.mouseSobre(pos_mouse):
                    main_menu()
                if botao_som.mouseSobre(pos_mouse):
                    som = True
        gameDisplay.fill(white)
        gameDisplay.blit(menu_simbolo1, (200, 200))
        gameDisplay.blit(menu_simbolo2, (800, 350))
        gameDisplay.blit(menu_simbolo3, (100, 450))
        gameDisplay.blit(fonteTituloJogo.render("Periodic.Py", 1, black), (440, 20))
        botao_som.desenhaBotao(gameDisplay, white)
        botao_voltar.desenhaBotao(gameDisplay, white)
        pygame.display.update()
        mainClock.tick(60)


def respostas():
    resposta = True
    while resposta:
        for event in pygame.event.get():
            pos_mouse = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar_resposta.mouseSobre(pos_mouse):
                    main_menu()
        gameDisplay.fill(white)
        gameDisplay.blit(menu_simbolo1, (200, 200))
        gameDisplay.blit(menu_simbolo2, (800, 350))
        gameDisplay.blit(menu_simbolo3, (100, 450))
        gameDisplay.blit(fonteTituloJogo.render("Periodic.Py", 1, black), (440, 20))
        gameDisplay.blit(fonteSugestao.render("Forma de jogar:", 1, black), (440, 150))
        gameDisplay.blit(fonteSugestao.render("Pressione o elemento, arraste", 1, black), (400, 200))
        gameDisplay.blit(fonteSugestao.render("até o frasco de Erlenmeyer e solte-o.", 1, black), (400, 230))
        gameDisplay.blit(fonteSugestao.render("Formulas utilizadas:", 1, black), (440, 270))
        gameDisplay.blit(fonteSugestao.render("Ácido Nítrico = HNO3", 1, black), (440, 300))
        gameDisplay.blit(fonteSugestao.render("Cloreto de Sódio = NaCl", 1, black), (440, 330))
        gameDisplay.blit(fonteSugestao.render("Ácido Sulfúrico = H2SO4", 1, black), (440, 360))
        gameDisplay.blit(fonteSugestao.render("Óxido Nitroso = N2O", 1, black), (440, 390))
        gameDisplay.blit(fonteSugestao.render("Água = H2O", 1, black), (440, 420))
        gameDisplay.blit(fonteSugestao.render("Gás Carbônico = CO2", 1, black), (440, 450))
        gameDisplay.blit(fonteSugestao.render("Amônia = NH3", 1, black), (440, 480))
        botao_voltar_resposta.desenhaBotao(gameDisplay, white)
        pygame.display.update()
        mainClock.tick(60)


def game():
    firstInit = True
    listaElementosSelecionados = []
    mostraMensagemTempo = 0
    pontuacao = 0
    vidas = 3
    gameExit = False

    def mostrarvidas():
        fonte = pygame.font.SysFont('comicsansms', 20)
        corrente = "Vidas: " + str(vidas).zfill(2)
        texto = fonte.render(corrente, True, black)
        texto_rect = texto.get_rect()
        texto_rect.topright = [100, 0]
        gameDisplay.blit(texto, texto_rect)

    while not gameExit:
        gameDisplay.fill(gray)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

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
                                        gameExit = False
                                        fimdejogo = False
                                        vidas = 3
                                        pontuacao = 0
                                    if botao_voltar_menu.mouseSobre(pos_mouse):
                                        main_menu()
                            exibe_fim1 = fonteTituloJogo.render("Fim de Jogo!", True, black)
                            exibe_fim2 = fonteMensagem.render(
                                ("Jogador: " + nome + "          Pontos Obtidos:" + str(pontuacao)), True,
                                black)
                            gameDisplay.blit(exibe_fim1, (280, 30))
                            gameDisplay.blit(exibe_fim2, (196, 120))
                            mostraPontuacao()
                            botao_jogarNovamente.desenhaBotao(gameDisplay, white)
                            botao_voltar_menu.desenhaBotao(gameDisplay, white)

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

            # mostrar vida
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
                pygame.draw.rect(gameDisplay, black, [950, 632, 150, 50])
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
