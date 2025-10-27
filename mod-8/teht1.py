import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='linneag',
    password='3852335587',
    autocommit=True
)

def hae_lentokentta(icao, yhteys):
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()
    kursori.close()

    if tulos:
        print(f"Lentokenttä on {tulos[0]}, sijainti on {tulos[1]}.")


icao = input("Anna lentoaseman ICAO-koodi: ")
hae_lentokentta(icao, yhteys)

yhteys.close()



