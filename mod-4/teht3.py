# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.


arvo = input("Anna luku: ")

while arvo != "":
    print(f"Antamasi luku oli: {arvo}")
    arvo = input("Anna luku: ")

luku = float(arvo)
if luku < pienin:
        pienin = luku
if luku > suurin:
        suurin = luku

if luku == "":
    print(f"Pienin annettu luku oli: {pienin}")
    print(f"Suurin annettu luku oli: {suurin}")
