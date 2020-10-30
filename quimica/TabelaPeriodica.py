from ElementoQuimico import ElementoQuimico


class TabelaPeriodica:

    listaElementos = []

    def __init__(self):
        # Familia 1
        hidrogenio = ElementoQuimico('Hidrogênio', 0, 'H')
        litio = ElementoQuimico('Lítio', 1, 'Li')
        sodio = ElementoQuimico('Sódio', 1, 'Na')
        potassio = ElementoQuimico('Potássio', 1, 'K')
        rubidio = ElementoQuimico('Rubídio', 1, 'Rb')
        cesio = ElementoQuimico('Césio', 1, 'Cs')
        francio = ElementoQuimico('Frâncio', 1, 'Fr')

        # Familia 2
        berilio = ElementoQuimico('Berílio', 2, 'Be')
        magnesio = ElementoQuimico('Magnésio', 2, 'Mg')
        calcio = ElementoQuimico('Cálcio', 2, 'Ca')
        estroncio = ElementoQuimico('Estrôncio', 2, 'Sr')
        bario = ElementoQuimico('Bário', 2, 'Ba')
        radio = ElementoQuimico('Rádio', 2, 'Ra')

        # Familia 3
        escandio = ElementoQuimico('Escândio', 10, 'Sc')
        itrio = ElementoQuimico('Ítrio', 10, 'Y')
        lantanio = ElementoQuimico('Lantânio', 10, 'La')
        actinio = ElementoQuimico('Actínio', 10, 'Ac')

        # Familia 4
        titanio = ElementoQuimico('Titanio', 10, 'Ti')
        zirconio = ElementoQuimico('Zirconio', 10, 'Zr')
        halnio = ElementoQuimico('Hálnio', 10, 'Ha')
        kurchatovio = ElementoQuimico('Kurchatóvio', 10, 'Ku')

        # Familia 5
        vanadio = ElementoQuimico('Vanadio', 10, 'V')
        niobio = ElementoQuimico('Nióbio', 10, 'Nb')
        tantalo = ElementoQuimico('Tântalo', 10, 'Ta')
        hahnio = ElementoQuimico('Hâhnio', 10, 'Ha')

        # Familia 6
        cromo = ElementoQuimico('Cromo', 10, 'Cr')
        molibdenio = ElementoQuimico('Molibdênio', 10, 'Mo')
        tungstenio = ElementoQuimico('Tungstênio', 10, 'W')

        # Familia 7
        manganes = ElementoQuimico('Manganês', 10, 'Mn')
        tecnecio = ElementoQuimico('Tecnécio', 10, 'Tc')
        renio = ElementoQuimico('Rênio', 10, 'Re')

        # Familia 8
        ferro = ElementoQuimico('Ferro', 10, 'Fe')
        rutenio = ElementoQuimico('Rutênio', 10, 'Ru')
        osmio = ElementoQuimico('Ósmio', 10, 'Os')

        # Familia 9
        cobalto = ElementoQuimico('Cobalto', 10, 'Co')
        rhodio = ElementoQuimico('Rhódio', 10, 'Rh')
        iridio = ElementoQuimico('Irídio', 10, 'Ir')

        # Familia 10
        niquel = ElementoQuimico('Níquel', 10, 'Ni')
        paladio = ElementoQuimico('Paládio', 10, 'Pd')
        platina = ElementoQuimico('Platina', 10, 'Pt')

        # Familia 11
        cobre = ElementoQuimico('Cobre', 10, 'Cu')
        prata = ElementoQuimico('Prata', 10, 'Ag')
        ouro = ElementoQuimico('Ouro', 10, 'Au')

        # Familia 12
        zinco = ElementoQuimico('Zinco', 10, 'Zn')
        cadmio = ElementoQuimico('Cádmio', 10, 'Cd')
        mercurio = ElementoQuimico('Mercúrio', 10, 'Hg')

        # Familia 13
        boro = ElementoQuimico('Boro', 3, 'B')
        aluminio = ElementoQuimico('Alúminio', 3, 'Al')
        galio = ElementoQuimico('Gálio', 3, 'Ga')
        indio = ElementoQuimico('Indio', 3, 'In')
        talio = ElementoQuimico('Tálio', 3, 'Tl')

        # Familia 14
        carbono = ElementoQuimico('Carbono', 4, 'C')
        silicio = ElementoQuimico('Silício', 4, 'Si')
        germanio = ElementoQuimico('Germânio', 4, 'Ge')
        estanho = ElementoQuimico('Estanho', 4, 'Sn')
        chumbo = ElementoQuimico('Chumbo', 4, 'Pb')

        # Familia 15
        nitrogenio = ElementoQuimico('Nitrogênio', 5, 'N')
        fosforo = ElementoQuimico('Fósforo', 5, 'P')
        arsenio = ElementoQuimico('Arsênio', 5, 'As')
        antimonio = ElementoQuimico('Antimônio', 5, 'Sb')
        bismuto = ElementoQuimico('Bismuto', 5, 'Bi')

        # Familia 16
        oxigenio = ElementoQuimico('Oxigênio', 6, 'O')
        enxofre = ElementoQuimico('Enxofre', 6, 'S')
        selenio = ElementoQuimico('Selênio', 6, 'Se')
        telurio = ElementoQuimico('Telúrio', 6, 'Te')
        polonio = ElementoQuimico('Polônio', 6, 'Po')

        # Familia 17
        fluor = ElementoQuimico('Flúor', 7, 'F')
        cloro = ElementoQuimico('Cloro', 7, 'Cl')
        bromo = ElementoQuimico('Bromo', 7, 'Br')
        iodo = ElementoQuimico('Iodo', 7, 'I')
        astato = ElementoQuimico('Astato', 7, 'At')

        # Familia 18
        helio = ElementoQuimico('Hélio', 8, 'He')
        neonio = ElementoQuimico('Neônio', 8, 'Ne')
        argonio = ElementoQuimico('Argonio', 8, 'Ar')
        criptonio = ElementoQuimico('Criptônio', 8, 'Kr')
        xenonio = ElementoQuimico('Xenônio', 8, 'Xe')
        radonio = ElementoQuimico('Radonio', 8, 'Rn')

        for i in range(0, 18):
            self.listaElementos.append([])

        self.listaElementos[0].append(hidrogenio)
        self.listaElementos[0].append(litio)
        self.listaElementos[0].append(sodio)
        self.listaElementos[0].append(potassio)
        self.listaElementos[0].append(rubidio)
        self.listaElementos[0].append(cesio)
        self.listaElementos[0].append(francio)

        self.listaElementos[1].append(berilio)
        self.listaElementos[1].append(magnesio)
        self.listaElementos[1].append(calcio)
        self.listaElementos[1].append(estroncio)
        self.listaElementos[1].append(bario)
        self.listaElementos[1].append(radio)

        self.listaElementos[2].append(escandio)
        self.listaElementos[2].append(itrio)
        self.listaElementos[2].append(lantanio)
        self.listaElementos[2].append(actinio)

        self.listaElementos[3].append(titanio)
        self.listaElementos[3].append(zirconio)
        self.listaElementos[3].append(halnio)
        self.listaElementos[3].append(kurchatovio)

        self.listaElementos[4].append(vanadio)
        self.listaElementos[4].append(niobio)
        self.listaElementos[4].append(tantalo)
        self.listaElementos[4].append(hahnio)

        self.listaElementos[5].append(cromo)
        self.listaElementos[5].append(molibdenio)
        self.listaElementos[5].append(tungstenio)

        self.listaElementos[6].append(manganes)
        self.listaElementos[6].append(tecnecio)
        self.listaElementos[6].append(renio)

        self.listaElementos[7].append(ferro)
        self.listaElementos[7].append(rutenio)
        self.listaElementos[7].append(osmio)

        self.listaElementos[8].append(cobalto)
        self.listaElementos[8].append(rhodio)
        self.listaElementos[8].append(iridio)

        self.listaElementos[9].append(niquel)
        self.listaElementos[9].append(paladio)
        self.listaElementos[9].append(platina)

        self.listaElementos[10].append(cobre)
        self.listaElementos[10].append(prata)
        self.listaElementos[10].append(ouro)

        self.listaElementos[11].append(zinco)
        self.listaElementos[11].append(cadmio)
        self.listaElementos[11].append(mercurio)

        self.listaElementos[12].append(boro)
        self.listaElementos[12].append(aluminio)
        self.listaElementos[12].append(galio)
        self.listaElementos[12].append(indio)
        self.listaElementos[12].append(talio)

        self.listaElementos[13].append(carbono)
        self.listaElementos[13].append(silicio)
        self.listaElementos[13].append(germanio)
        self.listaElementos[13].append(estanho)
        self.listaElementos[13].append(chumbo)

        self.listaElementos[14].append(nitrogenio)
        self.listaElementos[14].append(fosforo)
        self.listaElementos[14].append(arsenio)
        self.listaElementos[14].append(antimonio)
        self.listaElementos[14].append(bismuto)

        self.listaElementos[15].append(oxigenio)
        self.listaElementos[15].append(enxofre)
        self.listaElementos[15].append(selenio)
        self.listaElementos[15].append(telurio)
        self.listaElementos[15].append(polonio)

        self.listaElementos[16].append(fluor)
        self.listaElementos[16].append(cloro)
        self.listaElementos[16].append(bromo)
        self.listaElementos[16].append(iodo)
        self.listaElementos[16].append(astato)

        self.listaElementos[17].append(helio)
        self.listaElementos[17].append(neonio)
        self.listaElementos[17].append(argonio)
        self.listaElementos[17].append(criptonio)
        self.listaElementos[17].append(xenonio)
        self.listaElementos[17].append(radonio)

    def desenhaTabelaPeriodica(self, gameDisplay):
        for i in range(0, len(self.listaElementos)):
            for j in range(0, len(self.listaElementos[i])):

                alturaInicial = 80
                paddingX = 30

                if i == 0:
                    alturaInicial = alturaInicial

                elif i == 1:
                    alturaInicial = alturaInicial + 75

                elif i >= 2 and i <= 11:
                    alturaInicial = alturaInicial + 75 * 3

                elif i >= 12 and i <= 16:
                    alturaInicial = alturaInicial + 75

                elif i == 17:
                    alturaInicial = alturaInicial

                elemento = self.listaElementos[i][j]

                elemento.x = paddingX+(i*60)
                elemento.y = alturaInicial+(j*75)

                elemento.desenhaElemento(gameDisplay, paddingX+(i*60),  alturaInicial+(j*75))

    def elementoClick(self, x, y):
        for i in range(0, len(self.listaElementos)):
            for j in range(0, len(self.listaElementos[i])):
                elemento = self.listaElementos[i][j]
                if x >= elemento.x and x <= elemento.x + elemento.base and y >= elemento.y and y <= elemento.y + elemento.altura:
                    return elemento
