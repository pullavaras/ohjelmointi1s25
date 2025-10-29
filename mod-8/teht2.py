import mysql.connector

def haku(maakoodi):
    sql = f"SELECT type, count(*) FROM airport where iso_country = '{maakoodi}' group by type"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"{rivi[0]} tyypin lentokenttiä on {rivi[1]} kappaletta.")
    return

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='linneag',
    password='3852335587',
    autocommit=True
)

maakoodi = input("Anna lentokentän maakoodi: ")
haku(maakoodi)

yhteys.close()








