nimi = input("Anna nimi: ")
nimet = set()

while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi")
    nimet.add(nimi)
    nimi = input("Anna nimi: ")

for n in nimet:
    print(n)