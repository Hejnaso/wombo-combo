#
# a = range(1, 101)
# i=0
# while i<len(a):
#     if a[i]%3==0 and a[i]%5==0:
#         print("bum-bác")
#     elif a[i]%3==0:
#         print ("bum")
#     elif a[i]%5==0:
#         print("bác")
#
#     else:
#         print(a[i])
#     i+=1


def faktorial(n):
    vysledek = n
    while n>1:
        n = n - 1
        vysledek = vysledek*n
    return vysledek



n = int(input("Zadej cislo pro vypocet faktorialu: "))
print(faktorial(n))


