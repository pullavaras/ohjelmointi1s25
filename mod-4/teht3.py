luku = input("Anna luku tai paina enter lopettaaksesi: ")

if int(luku):
    suurin = int(luku)
    pienin = int(luku)
    while True:
        luku = input("Anna luku tai paina enter lopettaaksesi: ")
        if luku == "":
            break
        luku = int(luku)
        if luku > suurin:
            suurin = luku
        if luku < pienin:
            suurin = luku
    print(f"Suurin luku: {suurin}\nPienin luku: {pienin}")


