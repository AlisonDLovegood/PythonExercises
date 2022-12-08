# Faça um algoritmo que peça dois números – base e expoente – calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

def pou(x, y):
    i = 0
    aux = x
    while i < y-1:
        aux *= x
        i += 1
    return aux


print('====================')
x = int(input('Digite o numerador: '))
y = int(input('Digite o expoente: '))
print(pou(x, y))
