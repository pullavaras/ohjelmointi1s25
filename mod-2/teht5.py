

leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))


luoti_g = luoti * 13.3
naula_g = naula * 32 * 13.3
leiviska_g = naula * 20 * 32 * 13.3

gramma = luoti_g + naula_g + leiviska_g
kilo = gramma / 1000

print(f"Massa nykymittojen mukaan:\n{kilo:.2f} kilogrammaa ja {gramma:.2f} grammaa.")


