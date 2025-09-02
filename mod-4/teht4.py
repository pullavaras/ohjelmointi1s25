# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
# Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa
# lukuaan arvauskertojen välissä.


import random

luku = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa numero yhden ja kymmenen väliltä: "))

    if arvaus == luku:
        print("Arvasit oikein!")
        break
    elif arvaus < luku:
        print("Liian pieni arvaus.")
    else:
        print("Liian suuri arvaus.")




