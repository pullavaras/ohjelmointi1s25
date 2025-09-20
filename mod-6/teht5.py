lista1 = [56, 234, 9, 4, 89, 43, 77, 303]

def parittomat(lista):
    lista2 = []
    for luku in lista:
        if luku % 2 == 0:
            lista2.append(luku)
    return lista2

parilliset = parittomat(lista1)

print(lista1)
print(parilliset)