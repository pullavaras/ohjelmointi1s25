#  Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon

yy_str = input("Anna ensimmäinen kokonaisluku: ")
yy = float(yy_str)

kaa_str = input("Anna toinen kokonaisluku: ")
kaa = float(kaa_str)

koo_str = input("Anna kolmas kokonaisluku: ")
koo = float(koo_str)

summa = yy + kaa + koo
tulo = yy * kaa * koo
keskiarvo = summa /3

print("Lukujen summa on " + str(summa))
print("Lukujen tulo on " + str(tulo))
print("Lukujen keskiarvo on " + str(keskiarvo))



