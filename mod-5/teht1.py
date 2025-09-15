import random

nopat = int(input("Anna noppien lukumäärä: "))

summa = 0

for i in range(nopat):
    silmäluku = random.randint(1,6)
    summa = summa + silmäluku

print(f"Silmälukujen summa oli {summa} ")