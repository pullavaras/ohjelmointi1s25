luvut = []

luku = input("Anna luku tai lopeta painamalla enter: ")

while luku != "":
    luku = int(luku)
    luvut.append(luku)
    luvut.sort(reverse=True)
    luku = input("Anna luku tai lopeta painamalla enter: ")


print(f"Viisi suurinta lukua oli: {luvut[0:5]}")
