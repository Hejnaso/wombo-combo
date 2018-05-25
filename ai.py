import random as rnd

def tah_ai(pole, symbol):

    if symbol == "x":
        while True:
            if "o" not in pole and len(pole) > 5:
                pozice = rnd.randrange(2, len(pole) - 3)
                return tah(pole, pozice, symbol)
            elif "o" not in pole and len(pole) < 6:
                pozice = rnd.randrange(0, len(pole) - 1)
                return tah(pole, pozice, symbol)

            if "x-x" in pole:
                pozice = pole.index("x-x") + 1
                return tah(pole, pozice, symbol)

            if "xx-" in pole:
                pozice = pole.index("xx-") + 2
                return tah(pole, pozice, symbol)

            if "-xx" in pole:
                pozice = pole.index("-xx")
                return tah(pole, pozice, symbol)

            if "oo-" in pole:
                pozice = pole.index("oo-") + 2
                return tah(pole, pozice, symbol)

            if "-oo" in pole:
                pozice = pole.index("-oo")
                return tah(pole, pozice, symbol)

            if "o-o" in pole:
                pozice = pole.index("o-o") + 1
                return tah(pole, pozice, symbol)

            if "--x" in pole:
                pozice = pole.index("--x") + 1
                return tah(pole, pozice, symbol)

            if "-x-" in pole:
                pozice = pole.index("-x-")
                return tah(pole, pozice, symbol)

            if "x--" in pole:
                pozice = pole.index("x--") + 1
                return tah(pole, pozice, symbol)

            if "-o-" in pole and (pole.index("-o-") != 0 or pole.index("-o-") != 1):
                pozice = pole.index("-o-")
                return tah(pole, pozice, symbol)

            if pole[1] == "o" and pole[2] == "-":
                pozice = 2
                return tah(pole, pozice, symbol)
            elif pole[-2] == "o" and pole[-3] == "-":
                pozice = -3
                return tah(pole, pozice, symbol)

            elif "---" in pole:
                pozice = pole.index("---") + 1
                return tah(pole, pozice, symbol)

            if "-o-" in pole and pole.index("-o-") != len(pole) - 2:
                pozice = pole.index("-o-")
                return tah(pole, pozice, symbol)

            if "o-" in pole and pole[0] != "-":
                pozice = pole.index("o-") + 1
                return tah(pole, pozice, symbol)
            if "-" in pole:
                pozice = pole.index("-")
                return tah(pole, pozice, symbol)

    else:
        while True:
            if "x" not in pole and len(pole) > 5:
                pozice = rnd.randrange(2, len(pole) - 3)
                return tah(pole, pozice, symbol)
            elif "x" not in pole and len(pole) < 6:
                pozice = rnd.randrange(0, len(pole) - 1)
                return tah(pole, pozice, symbol)

            if "o-o" in pole and pole.index("o-o") != len(pole)-1:
                print("chyba")
                pozice = pole.index("o-o") + 1
                return tah(pole, pozice, symbol)

            if "oo-" in pole:
                pozice = pole.index("oo-") + 2
                return tah(pole, pozice, symbol)

            if "-oo" in pole:
                pozice = pole.index("-oo")
                return tah(pole, pozice, symbol)

            if "xx-" in pole:
                pozice = pole.index("xx-") + 2
                return tah(pole, pozice, symbol)

            if "-xx" in pole:
                pozice = pole.index("-xx")
                return tah(pole, pozice, symbol)

            if "x-x" in pole:
                pozice = pole.index("x-x") + 1
                return tah(pole, pozice, symbol)

            if "--o" in pole:
                pozice = pole.index("--o") + 1
                return tah(pole, pozice, symbol)

            if "-o-" in pole:
                pozice = pole.index("-o-")
                return tah(pole, pozice, symbol)

            if "o--" in pole:
                pozice = pole.index("o--") + 1
                return tah(pole, pozice, symbol)

            if "-x-" in pole and (pole.index("-x-") != 0 or pole.index("-x-") != 1):
                pozice = pole.index("-x-")
                return tah(pole, pozice, symbol)

            if pole[1] == "x" and pole[2] == "-":
                pozice = 2
                return tah(pole, pozice, symbol)
            elif pole[-2] == "x" and pole[-3] == "-":
                pozice = -3
                return tah(pole, pozice, symbol)

            elif "---" in pole:
                pozice = pole.index("---") + 1
                return tah(pole, pozice, symbol)

            if "-x-" in pole and pole.index("-x-") != len(pole) - 2:
                pozice = pole.index("-x-")
                return tah(pole, pozice, symbol)

            if "x-" in pole and pole[0] != "-":
                pozice = pole.index("x-") + 1
                return tah(pole, pozice, symbol)

            if "-" in pole:
                pozice = pole.index("-")
                return tah(pole, pozice, symbol)





def tah(pole, pozice, symbol):
    return pole[:pozice]+symbol+pole[pozice+1:]