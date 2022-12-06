# fazer um algoritmo que calcule a soma e escreva a soma dos 50 primeiros termos dessa sequência: 1000/1, -997/3, 994/3, ...

num = 1000
count = 0
for den in range(1, 51):
    if den % 2 == 0:
        print(num, den)
        count += -num/den
    else:
        count += num/den
    num -= 3
print(f'soma: {count:.2f}')
