import random

syote = input("Kuinka monta pistettä arvotaan? ")

kokonaispisteet = int(syote)
ympyrän_sisällä = 0
pisteet = 0

while pisteet < kokonaispisteet:
    x = random.randint(-1000, 1000) / 1000
    y = random.randint(-1000, 1000) / 1000

    if x*x + y*y < 1:
        ympyrän_sisällä = ympyrän_sisällä + 1

    pisteet = pisteet + 1

pi_arvo = 4 * ympyrän_sisällä / kokonaispisteet
print(f"Piin likiarvo: {pi_arvo}")

