kerrat = 0

while kerrat <= 5:
    username = input("Anna käyttäjätunnus: ")
    password = input("Anna salasana: ")
    if  username == "python" and password == "rules":
        print("Tervetuloa.")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana.")
        kerrat = kerrat + 1
else:
    print("Pääsy evätty.")


