sukupuoli = input("Kerro biologinen sukupuolesi (mies/nainen): ")
hemoglobiini = int(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli == "mies":
    if 134 <= hemoglobiini < 195:
        print("Hemoglobiinitasosi on normaali.")
    elif hemoglobiini > 195:
        print("Hemoglobiinitasosi on korkea." )
    elif hemoglobiini < 134:
        print("Hemoglobiinitasosi on alhainen.")

if sukupuoli == "nainen":
    if 117 <= hemoglobiini < 175:
        print("Hemoglobiinitasosi on normaali.")
    elif hemoglobiini > 175:
        print("Hemoglobiinitasosi on korkea.")
    elif hemoglobiini < 117:
        print("Hemoglobiinitasosi on alhainen.")