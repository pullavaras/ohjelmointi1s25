luku = int(input("Anna luku ja ohjelma kertoo sinulle, onko se alkuluku: "))

alkuluku = True

for n in range(2, luku):
    if luku % n == 0:
        alkuluku = False
        break

if alkuluku:
    print(f"{luku} on alkuluku.")
else:
    print(f"{luku} ei ole alkuluku.")