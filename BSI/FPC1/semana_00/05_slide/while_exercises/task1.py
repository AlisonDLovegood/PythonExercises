# Crie um programa que lê as idades e alturas de alguns alunos. A condição de parada é a altura = 0. Em seguida, o programa deve informar quantos alunos com mais de 13 anos possuem altura inferior à 1,5.

alunos = []
print('========== REGRA ==========\n1. se a altura inserida for igual a zero, é apresentado o resultado e o programa encerra\n')
while True:
    aluno = []
    aluno.append(int(input('Digite sua idade: ')))
    aluno.append(float(input('Digite sua altura: ')))
    if aluno[1] == 0:
        break
    else:
        alunos.append(aluno)

count = 0
i = 0
while i < len(alunos):
    if alunos[i][0] > 13 and alunos[i][1] < 1.5:
        count += 1
    i += 1
print(f'{count} aluno(s) tem mais de 13 anos e altura inferior a um metro e meio.')
