def  litra(gallon):
    return gallon * 3.785

gallon = float(input("Anna gallonmäärä tai lopeta syöttämällä negatiivinen luku: "))

while gallon >= 0:
    litroja = litra(gallon)
    print(f"{gallon:.2f} gallonaa on {litroja:.2f} litraa.")
    gallon = float(input("Anna gallonmäärä tai lopeta syöttämällä negatiivinen luku: "))
