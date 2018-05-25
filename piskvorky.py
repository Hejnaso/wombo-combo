import ai


def vysledek(pole):
    if "xxx" in pole:
        print("Vyhrava hrac.")
        return False
    elif "ooo" in pole:
        print("Vyhrava AI.")
        return False
    elif "-" not in pole:
        print("Remiza")
        return False
    else:
        return True

def main():
    pole = 20*"-"
    symbol_ai = "o"
    symbol_vs = "x"

    AI = 0
    VS = 0

    print(len(pole))
    while "-" in pole:
        print("Hraje AI s O")
        pole = ai.tah_ai(pole,symbol_ai)
        if vysledek(pole) == False:
            print(pole)
            AI = AI+1
            break
        print(pole)
        print("Hraje AI s X")
        pole = ai.tah_ai(pole, symbol_vs)
        if vysledek(pole) == False:
            print(pole)
            VS = VS+1
            break
        print(pole)


def tah_hrace(pole):
    symbol = "x"
    invalid = True
    while invalid:
        try:
            pozice = int(input("Na kterou pozici chces hrat? "))
            if pozice < 0 or pozice > len(pole)-1:
                print("Jsi mimo (pole)...")
                invalid = True
            elif pole[pozice] != "-":
                print("To jdes s 'krizkem' po funuse!")
            else:
                invalid = False

        except ValueError:
            print("Toto neni platny vstup, vyber cislo z pole: ")

    return ai.tah(pole, pozice, symbol)

i=0
remiza = 0



while i < 200:
    main()
    i += 1