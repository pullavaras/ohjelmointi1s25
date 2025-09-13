leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

luoti = 13.3
naula = luoti * 32
leiviska = naula * 20

yhteensa = leiviskat * leiviska + naulat * naula + luodit * luoti
kg = yht // 1000
g = yht % 1000

print(f"Massa nykymittojen mukaan on {kg} kilogrammaa ja {g:.2f} grammaa.")
