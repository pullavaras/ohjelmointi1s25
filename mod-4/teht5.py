

käyttäjä = ("python")
salasana = ("rules")

mahd = 5
kokeiltu = 0

while kokeiltu < mahd:
    käyttäjä2 = input("Anna käyttäjätunnus: ")
    salasana2 = input("Anna salasana: ")
    if käyttäjä2 == käyttäjä and salasana2 == salasana:
        print("Tervetuloa.")
        break
    else:
        kokeiltu = kokeiltu + 1
else:
    print("Pääsy evätty.")

