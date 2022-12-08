# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
def produto(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] > lst[j] and i < j:
                lst.insert(i, lst.pop(j))
    return lst[0]


x = []
n = int(input('HOW MANY PURCHASES DO YOU WANT TO COMPARE? '))
for i in range(n):
    x.append(int(input('enter the price of one of them: ')))
print(f'Buy the one with that price: {produto(x)}')
