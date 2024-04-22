def befajl(nevek, pontok ,eredmeny):
    fr = open("alapvizsga1.txt", "r", encoding="UTF-8")
    maxpont = int(fr.readline().strip())
    sor = fr.readline().strip()
    while sor != "":
        adatok = sor.split("; ")
        nevek.append(adatok[0])
        pontok.append(int(adatok[1]))
        eredmeny.append(adatok[2])
        sor = fr.readline().strip()
    fr.close()
    return maxpont



def main():
    nevek, pontok , eredmeny= [], [] ,[]
    maxpont=befajl(nevek, pontok,eredmeny)
    print(nevek)
    print(pontok)
    print(eredmeny)
main()