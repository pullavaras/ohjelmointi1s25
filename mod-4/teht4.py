import random

oikein = random.randint(1,10)

pelaamassa = True

while pelaamassa:
    arvaus = int(input("Tee arvaus välillä 1-10: "))

    if arvaus == oikein:
        print("Oikein!")
        break
    elif arvaus > oikein:
        print("Liian suuri arvaus.")
    elif arvaus < oikein:
        print("Liian pieni arvaus.")

