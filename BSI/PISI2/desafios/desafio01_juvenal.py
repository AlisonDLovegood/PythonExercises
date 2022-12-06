def f(n, a, b):
    if n == 1:
        if n > a and n < b:
            g(chamadas)
        return 1
    elif n % 2 == 0:
        if n > a and n < b:
            g(chamadas)
        return f(n/2, a, b)
    else:
        if n > a and n < b:
            g(chamadas)
        return f(3*n+1, a, b)


def g(chamadas):
    chamadas.append(1)
    x = sum(chamadas)
    return x


chamadas = []
entradas = []
t = int(input())
for i in range(t):
    entradas.append(list(map(int, input().split())))

for i in range(len(entradas)):
    f(entradas[i][1], entradas[i][0], entradas[i][1])
    print(f'Caso {i+1}: {g(chamadas)-1}')
