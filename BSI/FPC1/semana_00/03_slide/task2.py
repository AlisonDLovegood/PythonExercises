# Ler três notas de um aluno, calcular a média e informar se ele foi aprovado (Média ≥ 7), reprovad (Média < 7) ou aprovado com louvor (Média = 10)

def media(x, y, z):
    average = (x+y+z)/3
    if average == 10:
        return 'Aprovado com merito'
    elif average > 7:
        return "Aprovado"
    else:
        return "Reprovado"


print(media(10, 10, 10))
