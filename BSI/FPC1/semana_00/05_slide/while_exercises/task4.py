# Faça um programa que identifica os 15 primeiros números primos (utilizando a instrução break).

primos = []
i = 1
while i <= 15:
    mult = 0

    j = 1
    while j <= i:
        if i % j == 0:
            mult += 1
        j += 1

    if (mult <= 2):
        primos.append(i)
    i += 1

print(*primos, sep=", ")
