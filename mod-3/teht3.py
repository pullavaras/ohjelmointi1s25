

sukupuoli = input("Kerro biologinen sukupuolesi (mies/nainen): ")
hemo = int(input("Kerro hemoglobiiniarvosi (g/l): "))

hemo_normaali_m = 134 <= hemo <= 195
hemo_normaali_n = 117 <= hemo <= 175

hemo_korkea_m = hemo > 195
hemo_korkea_n = hemo > 174

hemo_alhainen_m = hemo < 135
hemo_alhainen_n = hemo < 117

if sukupuoli == "mies":
    if hemo_normaali_m:
        print("Hemoglobiinitasosi on normaali.")
    elif hemo_korkea_m:
        print("Hemoglobiinitasosi on korkea.")
    else:
        print("Hemoglobiinitasosi on alhainen.")

if sukupuoli == "nainen":
    if hemo_normaali_n:
        print("Hemoglobiinitasosi on normaali.")
    elif hemo_korkea_n:
        print("Hemoglobiinitasosi on korkea.")
    else:
        print("Hemoglobiinitasosi on alhainen.")

