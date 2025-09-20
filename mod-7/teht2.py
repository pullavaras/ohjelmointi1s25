nimi = input("Anna nimi tai paina enter lopettaaksesi: ")

nimet = set()

while nimi != "":
    if nimi not in nimet:
        print(f"{nimi} on uusi nimi.")
        nimet.add(nimi)

    else:
        print(f"{nimi} on aiemmin syötetty nimi.")

    nimi = input("Anna nimi tai paina enter lopettaaksesi: ")

for n in nimet:
    print(n)