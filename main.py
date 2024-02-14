from random import randint

zu_erratende_zahl = randint(1,100)

ziel_zahl = -1

c=0


while zu_erratende_zahl != ziel_zahl:
    print("gib zahl : ")
    ziel_zahl = int(input())
    c = c+1

    if ziel_zahl > zu_erratende_zahl:
        print("die zahl ist kleiner")
    if ziel_zahl < zu_erratende_zahl:
        print("die zahl ist größer")


print("du hast die zahl erraten !!!! ", zu_erratende_zahl,ziel_zahl)
print(c,"Versuche")

