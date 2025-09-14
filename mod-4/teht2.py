tuumat = float(input("Anna tuumien määrä: "))

cm = 2.54 * tuumat

while tuumat >= 0:
    print(f"{tuumat} tuumaa on {cm:.2f} senttimetriä.")
    tuumat = float(input("Anna tuumien määrä: "))
    if tuumat < 0:
        break
