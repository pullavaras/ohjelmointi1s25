import random

montako = int(input("Kuinka monta arpakuutiota heitetään? "))

summa = 0

for n in range(montako):
    arpakuutio = random.randint(1,6)
    summa = summa + arpakuutio

print(f"Silmälukujen summa oli {summa}")