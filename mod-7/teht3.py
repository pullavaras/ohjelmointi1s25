lentoasemat = {}

while True:
    print("Valitse toiminto: syötä uusi lentoasema(1), hae vanha(2) tai lopeta(3): ")
    toiminto = int(input(""))

    if toiminto == 3:
        print("Toiminnot lopetettu.")
        break

    elif toiminto == 1:
        icao = input("Anna ICAO-koodi: ")
        lentoasema = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = lentoasema

    elif toiminto == 2:
        icao = input("Anna ICAO-koodi: ")
        if icao in lentoasemat:
            print(f"Tämä on lentoaseman {lentoasemat[icao]} ICAO-koodi.")
