kuha = float(input("Kuinka pitkä pyydystämäsi kuha on senttimetreissä? "))

alimitta = 37 - kuha

if kuha < 37:
    print(f"Kuha on {alimitta} senttimetriä liian lyhyt, laske se takaisin veteen.")
