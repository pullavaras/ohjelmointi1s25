import mysql.connector
from geopy import distance

def etäisyyden_haku(icao1, icao2):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao1}' OR ident = '{icao2}'"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount == 2:
        sijainti1, sijainti2 = tulos
        etäisyys = distance.distance(sijainti1, sijainti2).km
        print(f"Lentokenttien etäisyys on {etäisyys:.2f} kilometriä.")
    else:
        print("Virheelliset tiedot.")
    return

# pääohjelma
yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='linneag',
    password='3852335587',
    autocommit=True
)

icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-koodi: ")
etäisyyden_haku(icao1, icao2)

yhteys.close()