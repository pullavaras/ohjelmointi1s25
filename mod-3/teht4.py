vuosi = int(input("Anna vuosi: "))

if vuosi % 4 == 0:
    print(f"{vuosi} on karkausvuosi.")

if vuosi % 100 == 0:
    if vuosi % 400 == 0:
        print(f"{vuosi} on karkausvuosi.")

else:
    print(f"{vuosi} ei ole karkausvuosi.")
