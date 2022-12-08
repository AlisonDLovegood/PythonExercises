# Escreva um programa que lê uma quantidade indeterminada de números inteiros e escreve todos os que forem ímpares positivos (use o‘continue’. Considerar o valor 99 como fim da entrada.

print('========== REGRA ==========\n1. se o número digitado for 99, é apresentado o resultado e o programa encerra\n')
imp_pos = []
while True:
    n = int(input('Digite um nº inteiro: '))
    if n == 99:
        break
    elif n % 2 != 0 and n > 0:
        imp_pos.append(n)
    else:
        continue
print(*imp_pos, sep=", ")
