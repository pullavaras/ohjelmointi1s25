import random

def noppa():
    return random.randint(1, 6)

pelaamassa = True
while pelaamassa:
    kuusi = noppa()
    print(f"silmäluku: {kuusi}")
    if kuusi == 6:
        pelaamassa = False





