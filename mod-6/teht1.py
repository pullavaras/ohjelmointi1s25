import random
pelaamassa = True

def noppa():
    return random.randint(1,6)

while pelaamassa:
    silmaluku=noppa()
    print(f"Silmäluku oli: {silmaluku}")
    if silmaluku == 6:
        break





