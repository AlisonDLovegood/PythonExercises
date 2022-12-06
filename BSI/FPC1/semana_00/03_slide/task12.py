# Fazer um algoritmo para calcular e escrever a seguinte soma: 37x38/1 + 36x37/2 + 35x36/3 + ... + 1x2/37
soma = 0
num1 = 37
num2 = 38
for den in range(1, 38):
    soma += (num1*num1)/den
    num1 -= 1
    num2 -= 1
print(f'Soma: {soma:.2f}')
