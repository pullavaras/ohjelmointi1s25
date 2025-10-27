import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='linneag',
    password='3852335587',
    autocommit=True
    )

def lentokentat(maakoodi, yhteys):
    sql = "SELECT type, COUNT(*) AS maara FROM airport Where iso_country = %s GROUP BY type"
    kursori = yhteys.cursor()
    kursori.execute(sql, (maakoodi,))
    tulos = kursori.fetchall()
    kursori.close()

    print(f"Lentokentät maassa {maakoodi}:")
    for tyyppi, maara in tulos:
        print(f"Status: {tyyppi}, {maara} kpl")


maa = input("Anna maakoodi: ")
lentokentat(maa, yhteys)

yhteys.close()









