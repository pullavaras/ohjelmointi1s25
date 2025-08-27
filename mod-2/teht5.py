#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

#   Yksi leiviskä on 20 naulaa.
#   Yksi naula on 32 luotia.
#   Yksi luoti on 13,3 grammaa.

leiviskat = input("Anna leiviskät.\n")
leiviskat = float(leiviskat)

naulat = input("Anna naulat.\n")
naulat = float(naulat)

luodit = input("Anna luodit.\n")
luodit = float(luodit)

luoti = 13.3
naula = luoti * 32
leiviska = naula * 20

paino_yht = leiviskat * leiviska + naulat * naula + luodit * luoti
kilo = paino_yht / 1000
gramma = kilo * 1000

print("Massa nykymittojen mukaan:")
print(f"{kilo:.2f} kilogrammaa ja {gramma:.2f} grammaa.")


