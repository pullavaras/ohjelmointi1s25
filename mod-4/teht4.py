import random

oikea_arvaus = random.randint(1,10)

while True:
    arvaus = int(input("Arvaa numero välillä 1-10: "))
    if arvaus == oikea_arvaus:
        print("Arvasit oikein!")
        break
    elif arvaus < oikea_arvaus:
        print("Liian pieni arvaus.")
    elif arvaus > oikea_arvaus:
        print("Liian suuri arvaus.")
