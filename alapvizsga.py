from random import *

def befajl(nevek, pontok ,eredmeny):
    a  = input("Melyik txt-t nyissa meg?")
    fr = open( a, "r", encoding="UTF-8")
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
    b= input("Akarsz e irni ??")
    if b=="igen":
        a= input("Melyiket ?")
        fa=open( a, "a",encoding="UTF-8")
        c=input("név?")
        d=int(input("pontok?"))
        if d >= 48:
            e = "igen"
        else:
            e = "nem"
        nevek.append(c)
        pontok.append(d)
        eredmeny.append(e)
        fa.write(f"{c} ; {d} ; {e}")


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

#megszámolás
def sikeres_vizsgak(eredmeny):
    db = 0
    n = len(eredmeny)
    for i in range(n):
        if eredmeny[i] == "igen":
            db += 1

    return db

def atlag(pontok):
    n=len(pontok)
    ossz=0
    for i in range(n):
        ossz+=pontok[i]
    c=ossz/n
    print("Az átlag:",c)



def kivalogat(nevek, eredmeny):
    atjutott_nevei = []
    for i in range(len(nevek)):
        if eredmeny[i] == "igen" and not bennevan(nevek[i], atjutott_nevei):
            atjutott_nevei.append(nevek[i])
        
    return atjutott_nevei

def bennevan(elem, lista):
    i = 0
    while i < len(lista) and not(lista[i] == elem):
        i += 1
    return i < len(lista)



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
    n=len(pontok)
    i=0
    while i < n and not(pontok[i] == 120):
        i += 1
    if i < n:
        print(nevek[i])
    else:
        print("Nincs ilyen a listában! ")

def r_szam(nevek):
    n = len(nevek)
    r = randint(1,n)

    return nevek[r]



def main():
    nevek, pontok , eredmeny= [], [] ,[]
    maxpont = befajl(nevek, pontok, eredmeny)
    rendez(nevek, pontok,eredmeny)
    hozafuzes(nevek, pontok, eredmeny)
    db = sikeres_vizsgak(eredmeny)
    atlag(pontok)
    atjutottak = kivalogat(nevek, eredmeny)
    mini = min(nevek, pontok)
    maxi = max(nevek, pontok)
    kereses(pontok,nevek)
    random_sorsolt = r_szam(nevek)
    print(nevek)
    print(pontok)
    print(eredmeny)
    print("Ennyi a sikeres alapvizsga:",db)
    print(random_sorsolt)
    print()
    print("A legtöbb pontot elért tanulo:", maxi)
    print("A legkevesebbet pontot elért tanulo:", mini)


main()