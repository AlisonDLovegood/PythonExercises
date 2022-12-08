"""
    Tem-se um conjunto de dados
    contendo a altura e o sexo (M ou F) de
    15 pessoas. Faça um programa que
    calcule e mostre:
        – a maior e a menor altura do grupo
        – a média de altura das mulheres
        – o número de homens
        – o sexo da pessoa mais alta
"""


pessoa1 = {'altura': 1.9, 'sexo': 'M'}
pessoa2 = {'altura': 1.5, 'sexo': 'M'}
pessoa3 = {'altura': 1.5, 'sexo': 'F'}
pessoa4 = {'altura': 1.5, 'sexo': 'M'}
pessoa5 = {'altura': 1.5, 'sexo': 'M'}
pessoa6 = {'altura': 1.5, 'sexo': 'M'}
pessoa7 = {'altura': 1.5, 'sexo': 'F'}
pessoa8 = {'altura': 1.1, 'sexo': 'M'}
pessoa9 = {'altura': 1.5, 'sexo': 'M'}
pessoa10 = {'altura': 1.5, 'sexo': 'M'}
pessoa11 = {'altura': 1.5, 'sexo': 'F'}
pessoa12 = {'altura': 1.5, 'sexo': 'M'}
pessoa13 = {'altura': 1.5, 'sexo': 'M'}
pessoa14 = {'altura': 1.5, 'sexo': 'M'}
pessoa15 = {'altura': 1.5, 'sexo': 'M'}

pessoas = {1:   pessoa1,
           2:   pessoa2,
           3:   pessoa3,
           4:   pessoa4,
           5:   pessoa5,
           6:   pessoa6,
           7:   pessoa7,
           8:   pessoa8,
           9:   pessoa9,
           10:	pessoa10,
           11:	pessoa11,
           12:	pessoa12,
           13:	pessoa13,
           14:	pessoa14,
           15:	pessoa15
           }

maior, sexo, menor, count_idades_m, count_h = 0, '', 2.5, 0, 0

for i in range(1, len(pessoas)+1):
    if maior < pessoas[i]['altura']:
        maior = pessoas[i]['altura']
        sexo = pessoas[i]['sexo']

    if menor > pessoas[i]['altura']:
        menor = pessoas[i]['altura']

    if pessoas[i]['sexo'] == 'M':
        count_idades_m += pessoas[i]['altura']

    if pessoas[i]['sexo'] == 'F':
        count_h += 1

print('====================================')
print(f'Maior altura = {maior}')
print(f'Menor altura = {menor}')
print(
    f'Media das alturas das mulheres = {count_idades_m/(len(pessoas)-count_h)}')
print(f'Nº de homens = {count_h}')
print(f'Sexo da pessoa mais alta = {sexo}')
