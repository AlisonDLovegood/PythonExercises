# Faça um Programa que leia três números e mostre-os em ordem decrescente.

def ordenar(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                aux = lst.pop(j)
                lst.insert(i, aux)
                i = 0
                j = 0
    return lst


x = []
for i in range(3):
    x.append(int(input()))
print(ordenar(x))
