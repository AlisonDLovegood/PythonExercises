# Fazer um algoritmo para calcular e escrever a soma dos cubos dos números pares compreendidos entre B e A (B > A).

a = int(input())
b = int(input())
soma = 0
for i in range(a, b):
    if i % 2 == 0:
        soma += i**3
print(soma)
