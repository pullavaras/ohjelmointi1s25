#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
#Ohjelma tulostaa suorakulmion piirin ja pinta-alan.


kanta_str = input('Anna suorakulmion kanta: ')
kanta = float(kanta_str)
korkeus_str = input('Anna suorakulmion korkeus: ')
korkeus = float(korkeus_str)

piiri = kanta * 2 + korkeus * 2
print("Suorakulmion piiri on " + str(piiri))

pintaala = kanta * korkeus
print("Suorakulmion pinta-ala on " + str(pintaala))

