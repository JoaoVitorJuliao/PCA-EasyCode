from ElementoQuimico import ElementoQuimico
from random import randint


class Pergunta:
    id = 0

    nomeCompostoQuimico = ''
    dica = ''

    listaElementos = []

    def defineElemento(self):
        if self.id == 1:
            self.acidosulfurico()
        elif self.id == 2:
            self.cloretosodio()
        elif self.id == 3:
            self.acidoacetico()
        elif self.id == 4:
            self.oxidodinitrogeno()
        elif self.id == 5:
            self.agua()
        elif self.id == 6:
            self.gascarbonico()
        elif self.id == 7:
            self.amonia()

    def acidosulfurico(self):
        hidrogenio = ElementoQuimico('Hidrogênio', 0, 'H')
        oxigenio = ElementoQuimico('Oxigênio', 6, 'O')
        enxofre = ElementoQuimico('Enxofre', 6, 'S')

        self.id = 1
        self.nomeCompostoQuimico = 'Ácido Sulfúrico'
        self.dica = 'Possui quatro oxigênios'

        self.listaElementos.append(hidrogenio)
        self.listaElementos.append(enxofre)
        self.listaElementos.append(oxigenio)

    def cloretosodio(self):
        cloro = ElementoQuimico('Cloro', 7, 'Cl')
        sodio = ElementoQuimico('Sódio', 1, 'Na')

        self.id = 2
        self.nomeCompostoQuimico = 'Cloreto de Sódio'
        self.dica = 'Possui um alcalino terroso'

        self.listaElementos.append(sodio)
        self.listaElementos.append(cloro)

    def acidoacetico(self):
        carbono = ElementoQuimico('Carbono ', 0, 'C')
        hidrogenio = ElementoQuimico('Hidrogênio ', 0, 'H')
        oxigenio = ElementoQuimico('Oxigênio ', 6, 'O')

        self.id = 3
        self.nomeCompostoQuimico = 'Ácido Acético'
        self.dica = 'Possui 2 Hidrogenios'

        self.listaElementos.append(hidrogenio)
        self.listaElementos.append(carbono)
        self.listaElementos.append(oxigenio)

    def oxidodinitrogeno(self):
        nitrogenio = ElementoQuimico('Nitrogênio ', 5, 'N')
        oxigenio = ElementoQuimico('Oxigênio ', 6, 'O')

        self.id = 4
        self.nomeCompostoQuimico = 'Óxido Dinitrogeno (Óxido Nitroso)'
        self.dica = 'Possui 2 nitrogenios'

        self.listaElementos.append(nitrogenio)
        self.listaElementos.append(oxigenio)

    def agua(self):
        hidrogenio = ElementoQuimico('Hidrogênio ', 0, 'H')
        oxigenio = ElementoQuimico('Oxigênio ', 6, 'O')

        self.id = 5
        self.nomeCompostoQuimico = 'Agua'
        self.dica = 'Possui 2 Hidrogenios'

        self.listaElementos.append(hidrogenio)
        self.listaElementos.append(oxigenio)

    def gascarbonico(self):
        carbono = ElementoQuimico('Carbono ', 0, 'C')
        oxigenio = ElementoQuimico('Oxigênio ', 6, 'O')

        self.id = 6
        self.nomeCompostoQuimico = 'gás carbônico'
        self.dica = 'Possui 2 oxigenios'

        self.listaElementos.append(carbono)
        self.listaElementos.append(oxigenio)

    def amonia(self):
        nitrogenio = ElementoQuimico('Nitrogênio ', 5, 'N')
        hidrogenio = ElementoQuimico('Hidrogênio ', 0, 'H')

        self.id = 7
        self.nomeCompostoQuimico = 'Amônia'
        self.dica = 'Possui 3 hidrogenios'

        self.listaElementos.append(nitrogenio)
        self.listaElementos.append(hidrogenio)

    def checarResposta(self, listaElementosSelecionado):

        if self.id == 1:
            qtdHidrogenio = 0
            qtdOxigenio = 0
            qtdEnxofre = 0

            for i in range(0, len(listaElementosSelecionado)):
                elemento = listaElementosSelecionado[i]
                if elemento.nomeElemento == 'Hidrogênio':
                    qtdHidrogenio = qtdHidrogenio + 1
                if elemento.nomeElemento == 'Oxigênio':
                    qtdOxigenio = qtdOxigenio + 1
                if elemento.nomeElemento == 'Enxofre':
                    qtdEnxofre = qtdEnxofre + 1

            if qtdHidrogenio == 2 and qtdOxigenio == 4 and qtdEnxofre == 1:
                return True
            else:
                return False

        if self.id == 2:
            qtdCloro = 0
            qtdSodio = 0

            for i in range(0, len(listaElementosSelecionado)):
                elemento = listaElementosSelecionado[i]
                if elemento.nomeElemento == 'Cloro':
                    qtdCloro = qtdCloro + 1
                if elemento.nomeElemento == 'Sódio':
                    qtdSodio = qtdSodio + 1

            if qtdSodio == 1 and qtdCloro == 1:
                return True
            else:
                return False

        if self.id == 3:
            qtdHidrogenio = 0
            qtdOxigenio = 0
            qtdCarbono = 0

            for i in range(0, len(listaElementosSelecionado)):
                elemento = listaElementosSelecionado[i]
                if elemento.nomeElemento == 'Hidrogênio':
                    qtdHidrogenio = qtdHidrogenio + 1
                if elemento.nomeElemento == 'Oxigênio':
                    qtdOxigenio = qtdOxigenio + 1
                if elemento.nomeElemento == 'Carbono':
                    qtdCarbono = qtdCarbono + 1

            if qtdHidrogenio == 2 and qtdOxigenio == 1 and qtdCarbono == 1:
                return True
            else:
                return False

        if self.id == 4:
            qtdOxigenio = 0
            qtdNitrogenio = 0

            for i in range(0, len(listaElementosSelecionado)):
                elemento = listaElementosSelecionado[i]
                if elemento.nomeElemento == 'Nitrogênio':
                    qtdNitrogenio = qtdNitrogenio + 1
                if elemento.nomeElemento == 'Oxigênio':
                    qtdOxigenio = qtdOxigenio + 1

            if qtdNitrogenio == 2 and qtdOxigenio == 1:
                return True
            else:
                return False

        if self.id == 5:
            qtdHidrogenio = 0
            qtdOxigenio = 0

            for i in range(0, len(listaElementosSelecionado)):
                elemento = listaElementosSelecionado[i]
                if elemento.nomeElemento == 'Hidrogênio':
                    qtdHidrogenio = qtdHidrogenio + 1
                if elemento.nomeElemento == 'Oxigênio':
                    qtdOxigenio = qtdOxigenio + 1

            if qtdHidrogenio == 2 and qtdOxigenio == 1:
                return True
            else:
                return False

        if self.id == 6:
            qtdcarbono = 0
            qtdOxigenio = 0

            for i in range(0, len(listaElementosSelecionado)):
                elemento = listaElementosSelecionado[i]
                if elemento.nomeElemento == 'Carbono':
                    qtdcarbono = qtdcarbono + 1
                if elemento.nomeElemento == 'Oxigênio':
                    qtdOxigenio = qtdOxigenio + 1

            if qtdcarbono == 1 and qtdOxigenio == 2:
                return True
            else:
                return False

        if self.id == 7:
            qtdnitrogenio = 0
            qtdhidrogenio = 0

            for i in range(0, len(listaElementosSelecionado)):
                elemento = listaElementosSelecionado[i]
                if elemento.nomeElemento == 'Nitrogênio':
                    qtdnitrogenio = qtdnitrogenio + 1
                if elemento.nomeElemento == 'Hidrogênio':
                    qtdhidrogenio = qtdhidrogenio + 1

            if qtdnitrogenio == 1 and qtdhidrogenio == 3:
                return True
            else:
                return False

    def novaPergunta(self):
        self.id = randint(1, 7)
        self.defineElemento()
