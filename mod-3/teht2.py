
hytti = input("Minkä hyttiluokan valitset; LUX, A, B, vai C? ")

if hytti == "LUX" or hytti == "Lux" or hytti == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")

elif hytti == "A" or hytti == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")

elif hytti == "B" or hytti == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")

elif hytti == "C" or hytti == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka. Valitse yksi listatuista luokista.")