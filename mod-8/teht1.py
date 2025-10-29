import mysql.connector

def haku(icao):
    sql = f'SELECT ident, municipality FROM airport where ident = "{icao}"'
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokentän {rivi[0]} sijaintikunta on {rivi[1]}.")
    return

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='linneag',
    password='3852335587',
    autocommit=True
)

icao = input("Anna lentokentän ICAO-koodi: ")
haku(icao)

yhteys.close()


