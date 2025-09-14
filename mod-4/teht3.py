luku = input("Anna luku: ")

if luku == "":
    print("Lukua ei annettu.")

else:
    luku = int(luku)
    pienin = luku
    suurin = luku

    while True:
        luku = input("Anna luku: ")

        if luku == "":
            break

        luku = int(luku)
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku


    print(f"Pienin luku oli {pienin} ja suurin luku oli {suurin}.")

