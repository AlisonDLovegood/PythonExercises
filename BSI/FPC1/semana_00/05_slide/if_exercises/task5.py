# Faça um Programa que leia três números e mostre-os em ordem decrescente.

def ordenar(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j] and i < j:
                lst.insert(i, lst.pop(j))
    return lst


x = []
n = int(input('HOW MANY NUMBERS DO YOU WANT TO ORDER? '))
for i in range(n):
    x.append(int(input('type it: ')))
print(ordenar(x))
