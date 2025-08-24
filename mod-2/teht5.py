#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

#   Yksi leiviskä on 20 naulaa.
#   Yksi naula on 32 luotia.
#   Yksi luoti on 13,3 grammaa.

leiviskat = input("Anna leiviskät ")
naulat = input("Anna naulat")
luodit = input("Anna luodit ")

leiviskat = float(leiviskat)
naulat = float(naulat)
luodit = float(luodit)

luoti = 13.3
naula = luoti * 32
leiviska = naula * 20


