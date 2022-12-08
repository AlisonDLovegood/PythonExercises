# Faça um Programa que peça para entrar com um ano (inteiro com 4 dígitos) e determine se o mesmo é ou não bissexto (divisível por 4).

def verificar(ano):
    bissexto = False
    if ano/4:
        bissexto = True
    return bissexto


print(verificar(2016))
