# Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#   kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#   nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

# Vihje: tutustu random.randint()-funktion käyttöön.

import random

numero1 = random.randint(0,9)
numero2 = random.randint(0,9)
numero3 = random.randint(0,9)

numero4 = random.randint(1,6)
numero5 = random.randint(1,6)
numero6 = random.randint(1,6)
numero7 = random.randint(1,6)


print(f"Ensimmäinen koodi on {numero1}" + f"{numero2}" + f"{numero3}")
print(f"Toinen koodi on {numero4}" + f"{numero5}" + f"{numero6}" + f"{numero7}")

