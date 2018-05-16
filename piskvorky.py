from GitHubProjects import ai


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
    pole = 12*"-"
    print(len(pole))
    while "-" in pole:
        pole = ai.tah_ai(pole)
        if vysledek(pole) == False:
            print(pole)
            break
        print(pole)
        pole = tah_hrace(pole)
        if vysledek(pole) == False:
            print(pole)
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

while i < 5:
    main()
    i += 1