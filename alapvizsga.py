def befajl(nevek, pontok ,eredmeny):
    fr = open("alapvizsga1.txt", "r", encoding="UTF-8")
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


def sikeres_vizsgak(eredmeny):
    db = 0
    n = len(eredmeny)
    for i in range(n):
        if eredmeny[i] == "igen":
            db += 1

    return db







def csere(x, i, j):
    x[i], x[j] = x[j], x[i]

def rendez(pontok,nevek,eredmeny):
    n = len(pontok)
    for i in range(n):
        for j in range(n-i-1):
            if pontok[j] > pontok[j+1]:
                csere(pontok, j, j+1)
                csere(nevek, j, j+1)
                csere(eredmeny, j, j+1)


def main():
    nevek, pontok , eredmeny= [], [] ,[]
    maxpont=befajl(nevek, pontok, eredmeny)
    rendez(nevek, pontok,eredmeny)
    db = sikeres_vizsgak(eredmeny)
    print(nevek)
    print(pontok)
    print(eredmeny)
    print(db)


main()