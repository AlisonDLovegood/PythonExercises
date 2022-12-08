# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda,etc.), se digitar outro valor deve aparecer valorinválido.

def dia(x):
    match x:
        case '1':
            return 'Domingo!'
        case '2':
            return 'SEGUNDA!'
        case '3':
            return 'TERÇA!'
        case '4':
            return 'QUARTA!'
        case '5':
            return 'QUINTA!'
        case '6':
            return 'SEXTA!'
        case '7':
            return 'SÁBADO!'
        case _:
            return 'VALOR INVÁLIDO!'


x = (input('Digite o número do dia da semana: '))
print(dia(x))
