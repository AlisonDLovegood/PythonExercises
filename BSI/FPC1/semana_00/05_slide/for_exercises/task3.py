"""
    Em uma eleição presidencial com 15 eleitores
    existem 3 candidatos. Os votos são informados por
    meio de código. Os códigos utilizados são:
    – 1 – Candidato A, 2 -Candidato B, 3 – Candidato C, 4 -
    Voto Nulo e 5 - Voto em Branco
    Faça um programa que leia os votos de cada eleitor,
    calcule e mostre:
            – O total de votos para cada candidato
            – O total de votos nulos
            – O total de votos em branco
            – A percentagem de votos nulos sobre o total de votos;
            – A percentagem
"""


print('============================================')
print('ELEIÇÃO NA CIDADE DE JERICHO, REGRAS:')
print('1. VOTAR EM A')
print('2. VOTAR EM B')
print('3. VOTAR EM C')
print('4. VOTAR EM NULO')
print('5. VOTAR EM BRANCO')
print('--------------------------------------------')
lst = []
for _ in range(10):
    lst.append(int(input('Digite sua opção: ')))
print('--------------------------------------------')
print(f'Total de votos em A: {lst.count(1)}')
print(f'Total de votos em B: {lst.count(2)}')
print(f'Total de votos em C: {lst.count(3)}')
print(f'Total de votos nulos: {lst.count(4)}')
print(f'Total de votos em branco: {lst.count(5)}')
print(f'Porcentagem de votos nulos: {(lst.count(4)*100)/len(lst):.2f}')
print(f'Porcentagem de votos em branco: {(lst.count(5)*100)/len(lst):.2f}')
