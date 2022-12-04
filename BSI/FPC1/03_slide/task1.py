# Determinar se um número é par ou ímpar e positivo ou negativo

def determinar(n):
    positivo = True
    par = True
    neutro = True
    if n % 2 != 0:
        par = False
    if n == 0:
        print(f'neutro: {neutro} \npar: {par}')
    elif n < 0:
        positivo = False
        print(f'positivo: {positivo} \npar: {par}')
    else:
        print(f'positivo: {positivo} \npar: {par}')


determinar(-5)
