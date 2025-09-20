import random

max = int(input("Mikä luku aseteteaan nopan maksimisilmäluvuksi: "))

def silmaluku(max):
    return random.randint(1, max)

pelaamassa = True

while pelaamassa:
    noppa = silmaluku(max)
    print(noppa)
    if noppa == max:
        break

