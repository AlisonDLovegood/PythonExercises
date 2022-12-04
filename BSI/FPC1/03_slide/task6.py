# Faça um algoritmo que lê uma temperatura em Fahrenheit e calcula a temperatura correspondente em Celsius. Ao final o programa deve exibir as duas temperaturas.

fahrenheit = float(input())
celcius = (5 * (fahrenheit-32) / 9)
print(f'Celcius: {fahrenheit} \nFahrenheit: {celcius:.2f}')
