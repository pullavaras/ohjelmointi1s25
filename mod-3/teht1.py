

kuha = float(input("Kuinka pitkä pyydystämäsi kuha on senttimetreissä? "))

alimitta = 37 - kuha
alimitta = str(alimitta)

if kuha < 37:
    print("Kuha on " + alimitta + " senttiä liian lyhyt. Laske se takaisin veteen.")
