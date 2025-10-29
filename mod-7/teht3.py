valinta = int(input("Syötä uuden lentoaseman tiedot (1), hae lentoasemaa (2) tai lopeta (3): "))
lentoasemat = {}

while valinta != 3:
    if valinta == 1:
        icao = input("Anna uuden lentokentän ICAO-koodi: ")
        nimi = input("Anna uuden lentokentän nimi: ")

        lentoasemat[icao] = nimi

    if valinta == 2:
        icao = input("Anna ICAO-koodi: ")
        if icao in lentoasemat:
            print(f"{icao} on lentoasema {lentoasemat[icao]}")
        else:
            print("Tuntematon ICAO-koodi.")
    valinta = int(input("Syötä uuden lentoaseman tiedot (1), hea lentoasemaa (2) tai lopeta (3): "))
