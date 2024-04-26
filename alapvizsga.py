from random import *

def befajl(nevek, pontok ,eredmeny):
    print()
    print("Az alábbi .txt állományok érhetőek el: ")
    print("--> alapvizsga_rovid.txt")
    print("--> alapvizsga_evfolyam.txt")
    print()
    a  = input("Melyik .txt állományban szeretnél dolgozni?\n")
    fr = open(a, "r", encoding="UTF-8")
    maxpont = int(fr.readline().strip())
    sor = fr.readline().strip()
    while sor != "":
        adatok = sor.split(" ; ")
        nevek.append(adatok[0])
        pontok.append(int(adatok[1]))
        eredmeny.append(adatok[2])
        sor = fr.readline().strip()

    fr.close()
    return maxpont 

def hozafuzes(nevek, pontok, eredmeny):
    print()
    b = input("A kiválasztott állományban szeretnél-e írni?\n(igen/nem): ")
    print()
    if b =="igen":
        a = input("Ismételd meg a fájl nevét!\n")
        print()
        fa = open(a, "a", encoding="UTF-8")
        c = input("Teljes neve: ")
        d = int(input("Alapvizsgán elért pontszám (0-120): "))
        print()
        if d >= 48:
            e = "igen"
        else:
            e = "nem"
        nevek.append(c)
        pontok.append(d)
        eredmeny.append(e)
        fa.write(f"{c} ; {d} ; {e}\n")


        fa.close()




def csere(x, i, j):
    x[i], x[j] = x[j], x[i]

def rendez(nevek, pontok, eredmeny):
    n = len(pontok)
    for i in range(n):
        for j in range(n - 1 - i):
            if pontok[j] < pontok[j+1]:
                csere(pontok, j , j+1)
                csere(nevek, j , j+1)
                csere(eredmeny, j , j+1)


def sikeres_vizsgak(eredmeny):
    db = 0
    n = len(eredmeny)
    for i in range(n):
        if eredmeny[i] == "igen":
            db += 1

    return db

def atlag(pontok):
    n = len(pontok)
    ossz = 0
    for i in range(n):
        ossz += pontok[i]
    c = ossz / n
    return c



def kivalogat(nevek, eredmeny):
    atjutott_nevei = []
    for i in range(len(nevek)):
        if eredmeny[i] == "igen":
            atjutott_nevei.append(nevek[i])
        
    return atjutott_nevei


def min(nevek, pontok):
    mini = 0
    for i in range(1, len(pontok)):
        if pontok[i] < pontok[mini]:
            mini = i
    return nevek[mini]


def max(nevek, pontok):
    maxi = 0
    for i in range(1, len(pontok)):
        if pontok[i] > pontok[maxi]:
            maxi = i
    return nevek[maxi]



def kereses(pontok, nevek):
    n = len(pontok)
    i = 0
    while i < n and not(pontok[i] == 120):
        i += 1
    if i < n:
        print("Aki maximális pontszámot ért el az alapvizsgán:", nevek[i])
    else:
        print("Senkinek se lett maximális pontszáma az alapvizsgán! ")


def r_szam(nevek):
    n = len(nevek)
    r = randint(1,n)
    return nevek[r]



def main():
    nevek, pontok, eredmeny = [], [] ,[]
    maxpont = befajl(nevek, pontok, eredmeny)
    hozafuzes(nevek, pontok, eredmeny)
    rendez(nevek, pontok, eredmeny)
    db = sikeres_vizsgak(eredmeny)
    atl=atlag(pontok)
    atjutottak = kivalogat(nevek, eredmeny)
    mini = min(nevek, pontok)
    maxi = max(nevek, pontok)
    kereses(pontok, nevek)
    random_sorsolt = r_szam(nevek)

    print()
    print("Diákok, akik részt vettek az alapvizsgán: ")
    print(nevek)
    print()
    print("A diákok pontszámai:")
    print(pontok)
    print()
    print("Sikerült-e a diáknak átjutni a vizsgán? ")
    print(eredmeny)
    print()
    print("Sikeres alapvizsgák száma:", db)
    print()
    print("Az átjutottak nevei:", atjutottak)
    print()
    print("A legtöbb pontot elért tanulo:", maxi)
    print()
    print("A legkevesebb pontot elért tanulo:", mini)
    print()
    print("Az alapvizsgán szerzett pontok átlaga:", round(atl, 1))
    print()
    print("Egy kisorsolt név a névsorból, aki kap egy csokit:", random_sorsolt)



main()