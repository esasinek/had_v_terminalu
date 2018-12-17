from random import randrange

souradnice_hada = [(0, 0), (1, 0), (2, 0)]
velikost_pole = [10, 30]    # radky, sloupce
seznam_ovoce = [(5, 7)]
pocet_tahu = 0

def vytvor_mapu(souradnice_hada, seznam_ovoce):
    mapa = []
    for zn in range(velikost_pole[0]):
        radek = []
        for ra in range(velikost_pole[1]):
            radek.append(". ")              # vytečkované pole
        mapa.append(radek)
    for x, y in souradnice_hada:                 # had
        mapa[y][x] = "X "
    for w, z in seznam_ovoce:
        mapa[z][w] = "? "
    return mapa


def nakresli_mapu(mapa):
    for radek in mapa:
        print("".join(radek))              # oddělení na řádky


def uvnitr_pole(pozice):
    """
    Tato funkce zjišťuje, jestli nové souřadnice po zadání inputu od uživatele jsou ještě uvnitř pole,
    # tzn. jestli had náhodou nechce vyjet ven z pole.
    """
    if 0 > pozice[0] or pozice[0] > velikost_pole[1]:
        return False
    if 0 > pozice[1] or pozice[1] > velikost_pole[0]:
        return False
    return True


def pohyb(souradnice, strana):
    """
    Tato funkce umožňuje hadovi pohyb tím, že přijme aktuální souřadnice a světovou stranu,
    a následně upraví souřadnice udávající umístění hada.
    Prakticky vezme množinu dvojic čísel, přidá novou dvojici na konec a první dvojici smaže.
    """
    global seznam_ovoce
    global pocet_tahu
    mapa = vytvor_mapu(souradnice_hada, seznam_ovoce)
    x = souradnice[-1][0]
    y = souradnice[-1][1]
    if strana == "v":
        x += 1
    elif strana == "j":
        y += 1
    elif strana == "s":
        y -= 1
    elif strana == "z":
        x -= 1
    nova = x, y                     # nová dvojice souřadnic
    try:
        if nova in souradnice:          # pokud uživatel hraje do vlastního těla
            raise ValueError("Game over", "Sežral sis hlavu.")
        elif not uvnitr_pole(nova):     # pokud uživatel hraje mimo hrací pole
            raise ValueError("Game over", "Narazil jsi do zdi.")
        elif nova in seznam_ovoce:
            seznam_ovoce.remove(nova)
            souradnice.append(nova)
        else:
            souradnice.append(nova)
            souradnice.pop(0)
    finally:
        pocet_tahu += 1
        if pocet_tahu % 30 == 0:
            while True:
                x = randrange(velikost_pole[0])
                y = randrange(velikost_pole[1])
                nove_ovoce = x, y
                if nove_ovoce not in souradnice:
                    seznam_ovoce.append(nove_ovoce)
                    break
    return souradnice, pocet_tahu, seznam_ovoce
