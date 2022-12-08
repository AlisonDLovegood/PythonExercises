# fatorial

def fatorial(x):
    fat = 1
    i = 1
    while i <= x:
        fat *= i
        i += 1
    return fat


x = int(input('Digite um nº para calcular seu fatorial: '))
print(fatorial(x))
