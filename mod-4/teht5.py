kayttajatunnus = "python"
salasana = "rules"

yritykset = 0

while yritykset < 5:
    kayttaja_k = input("Anna käyttäjätunnus: ")
    kayttaja_s = input("Anna salasana: ")

    if kayttaja_k == kayttajatunnus and kayttaja_s == salasana:
        print("Tervetuloa.")
        break

    else:
        print("Käyttäjätunnus tai salasana väärin.")
        yritykset = yritykset + 1

else:
    print("Pääsy evätty.")

