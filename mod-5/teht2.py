luvut = []

numero = input("Anna luku tai lopeta painamalla enter: ")

while numero != "":
    luku = int(numero)
    luvut.append(luku)
    numero = input("Anna luku tai lopeta painamalla enter: ")

luvut.sort(reverse = True)

print(f"Viisi suurinta lukua olivat {luvut[0:5]}.")