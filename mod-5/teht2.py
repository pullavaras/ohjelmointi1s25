lista = []

luku = input("Anna luku tai paina enter lopettaaksesi: ")

while luku != "":
    luku = int(luku)
    lista.append(luku)
    lista.sort(reverse = True)
    luku = input("Anna seuraava luku tai paina enter lopettaaksesi: ")

print(f"Viisi suurinta lukua: {lista[0:6]}")
