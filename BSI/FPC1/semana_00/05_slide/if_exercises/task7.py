def turno(x):
    match x:
        case 'M':
            return 'BOM DIA!!'
        case 'T':
            return 'BOA TARDE!!'
        case 'N':
            return 'BOA NOITE!!'
        case _:
            return 'VALOR INVÁLIDO!'


x = (input('Qual horário você estuda? '))
print(turno(x))
