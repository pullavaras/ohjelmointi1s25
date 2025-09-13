sukupuoli = input("Kerro biologinen sukupuolesi (mies/nainen): ")
hg = int(input("Anna hemoglobiiniarvo: "))

if sukupuoli == ("mies" and hg < 134) or ("nainen" and hg < 117):
    print("Hemoglobiiniarvosi on alhainen.")
elif sukupuoli == ("mies" and hg > 195) or ("nainen" and hg > 175):
    print("Hemoglobiiniarvosi on korkea.")
else:
    print("Hemoglobiiniarvosi on normaali.")