# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä
# antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa.
# 1 tuuma = 2,54 cm


tuumat = float(input("Anna tuumat: "))

cm = tuumat * 2.54

while tuumat > 0:
    print(f"{tuumat} tuumaa on {cm} senttimetriä.")
    tuumat = float(input("Anna tuumat: "))
    if tuumat < 0:
        break

