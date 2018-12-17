from had import *

print("Zahrajeme si hada.")

try:
    povel = "nic"
    mapa = vytvor_mapu(souradnice_hada, seznam_ovoce)
    nakresli_mapu(mapa)
    while povel != "konec":
        povel = input("Zadej světovou stranu, na kterou má had jet (s, v, j nebo z):\n")
        if povel in ["s", "v" , "j", "z"]:
            souradnice_hada, pocet_tahu, ovoce = pohyb(souradnice_hada, povel)
            mapa = vytvor_mapu(souradnice_hada, seznam_ovoce)
            nakresli_mapu(mapa)
        else:
            print("To je špatně. Zadej písmeno s, v, j nebo z.\nChceš-li ukončit hru, napiš 'konec'.")
    if povel == "konec":
        raise ValueError("Konec hry")

except ValueError as e:
    if e.args[0] == "Game over":
        print("Konec hry.")
        print(e.args[1])
    else:
        raise
