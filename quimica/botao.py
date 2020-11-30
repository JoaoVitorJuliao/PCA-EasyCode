import pygame


class Botao:
    def __init__(self, **kargs):
        self.cor = kargs.get('cor')
        self.posx = kargs.get('posx')
        self.posy = kargs.get('posy')
        self.largura = kargs.get('largura')
        self.altura = kargs.get('altura')
        self.texto = kargs.get('texto')

    def mouseSobre(self, pos):
        if self.posx < pos[0] < self.posx + self.largura:
            if self.posy < pos[1] < self.posy + self.altura:
                return True
        return False

    def desenhaBotao(self, gameDisplay, cor):
        pygame.draw.rect(gameDisplay, self.cor, (self.posx, self.posy, self.largura, self.altura))
        fonte=pygame.font.SysFont('comicsansms', 20)
        texto_menu=fonte.render(self.texto, True, cor)
        gameDisplay.blit(texto_menu, (self.posx + (self.largura/2 - texto_menu.get_width()/2), self.posy + (self.altura/2-texto_menu.get_height()/2)))
