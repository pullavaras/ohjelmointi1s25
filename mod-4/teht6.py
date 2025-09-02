import random

numero = int(input("Kuinka monta osumaa? "))

i = 0
osumat = 0
while 1 < numero:
    x = random.random()
    y = random.random()
    if x * x + y * y < 1:
        osumat = osumat + 1
    i = i + 1
pi = 4 * osumat / numero
print(f"Piin arvo: {pi}")