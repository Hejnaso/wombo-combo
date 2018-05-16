# def nacti_cislo():
#     odpoved = input("Zadej cislo: ")
#     try:
#         cislo = 11/int(odpoved)
#     except ZeroDivisionError:
#         cislo = 11/0.00000001
#         print("Deleni nulou, delim namisto toho infiminitezalnim cimsi.")
#     except ValueError:
#         cislo = 0
#         print("Deleni pismenem nejde, nastavim nulu")
#
#     print("Cislo je: {}".format(cislo))
#
# nacti_cislo()

#####    AI   #####

import random

def tah_pocitace(pole):
    pozice = random.randrange(len(pole))
    symbol = 'o'
    return tah(pole, pozice, symbol)

def tah(pole, pozice, symbol):
    return pole[:pozice] + symbol + pole[pozice+1:]