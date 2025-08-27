
# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

kala = input("Kuinka pitkä kalastamasi kuha on senttimetreissä? ")
kala = float(kala)

alipaino = 37 - kala
alipaino = str(alipaino)

if kala < 37:
    print("Laske kuha taikaisin veteen. Kuha on " + alipaino + " senttiä alimittainen.")

