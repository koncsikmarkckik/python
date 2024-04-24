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

def main():
    nevek, pontok , eredmeny= [], [] ,[]
    maxpont = befajl(nevek, pontok, eredmeny)
    db = sikeres_vizsgak(eredmeny)
    print(nevek)
    print(pontok)
    print(eredmeny)
    print(db)


main()