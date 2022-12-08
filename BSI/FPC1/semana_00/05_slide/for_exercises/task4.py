# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

lst = []
print('============================================')
print('CONFERIR QUANTIDADE DE ÍMPAR E PAR EM ENTRADAS')
for _ in range(10):
    lst.append(int(input('Digite um número: ')))

count = 0
for i in range(len(lst)):
    if lst[i] % 2 == 0:
        count += 1
print('--------------------------------------------')
print(f'Quantidade de pares: {count}')
print(f'Quantidade de ímpares: {len(lst)-count}')
