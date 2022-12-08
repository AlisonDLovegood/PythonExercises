"""
    Tem-se um conjunto de dados
    contendo a altura e o sexo (masculino,
    feminino) de 50 pessoas. Fazer um
    algoritmo que calcule e escreva:
        • - a maior e a menor altura do grupo;
        • - a média de altura das mulheres;
        • - o número de homens;
        • -A porcentagem de homens e de
    mulheres.
"""


def maior(lst):
    mai = 0
    for i in range(len(lst)):
        if mai < lst[i]:
            mai = lst[i]
    return mai


def menor(lst):
    men = 2.5
    for i in range(len(lst)):
        if men > lst[i]:
            men = lst[i]
    return men


def porcentagem(n, lst):
    x = (n*100)/len(lst)
    return x


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
pessoa16 = {'altura': 1.5, 'sexo': 'M'}
pessoa17 = {'altura': 1.5, 'sexo': 'M'}
pessoa18 = {'altura': 1.5, 'sexo': 'M'}
pessoa19 = {'altura': 1.5, 'sexo': 'M'}
pessoa20 = {'altura': 1.5, 'sexo': 'M'}
pessoa21 = {'altura': 1.5, 'sexo': 'F'}
pessoa22 = {'altura': 1.5, 'sexo': 'F'}
pessoa23 = {'altura': 1.5, 'sexo': 'F'}
pessoa24 = {'altura': 1.5, 'sexo': 'F'}
pessoa25 = {'altura': 1.5, 'sexo': 'M'}
pessoa26 = {'altura': 1.5, 'sexo': 'M'}
pessoa27 = {'altura': 1.5, 'sexo': 'M'}
pessoa28 = {'altura': 1.5, 'sexo': 'M'}
pessoa29 = {'altura': 1.5, 'sexo': 'M'}
pessoa30 = {'altura': 1.5, 'sexo': 'F'}
pessoa31 = {'altura': 1.5, 'sexo': 'M'}
pessoa32 = {'altura': 1.5, 'sexo': 'M'}
pessoa33 = {'altura': 1.5, 'sexo': 'M'}
pessoa34 = {'altura': 1.5, 'sexo': 'M'}
pessoa35 = {'altura': 1.5, 'sexo': 'M'}
pessoa36 = {'altura': 1.5, 'sexo': 'M'}
pessoa37 = {'altura': 1.5, 'sexo': 'F'}
pessoa38 = {'altura': 1.5, 'sexo': 'F'}
pessoa39 = {'altura': 1.5, 'sexo': 'M'}
pessoa40 = {'altura': 1.5, 'sexo': 'M'}
pessoa41 = {'altura': 1.5, 'sexo': 'M'}
pessoa42 = {'altura': 1.5, 'sexo': 'M'}
pessoa43 = {'altura': 1.5, 'sexo': 'M'}
pessoa44 = {'altura': 1.5, 'sexo': 'F'}
pessoa45 = {'altura': 1.5, 'sexo': 'M'}
pessoa46 = {'altura': 1.5, 'sexo': 'F'}
pessoa47 = {'altura': 1.5, 'sexo': 'M'}
pessoa48 = {'altura': 1.5, 'sexo': 'F'}
pessoa49 = {'altura': 1.5, 'sexo': 'M'}
pessoa50 = {'altura': 1.5, 'sexo': 'M'}
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
           15:	pessoa15,
           16:	pessoa16,
           17:	pessoa17,
           18:	pessoa18,
           19:	pessoa19,
           20:	pessoa20,
           21:	pessoa21,
           22:	pessoa22,
           23:	pessoa23,
           24:	pessoa24,
           25:	pessoa25,
           26:	pessoa26,
           27:	pessoa27,
           28:	pessoa28,
           29:	pessoa29,
           30:	pessoa30,
           31:	pessoa31,
           32:	pessoa32,
           33:	pessoa33,
           34:	pessoa34,
           35:	pessoa35,
           36:	pessoa36,
           37:	pessoa37,
           38:	pessoa38,
           39:	pessoa39,
           40:	pessoa40,
           41:	pessoa41,
           42:	pessoa42,
           43:	pessoa43,
           44:	pessoa44,
           45:	pessoa45,
           46:	pessoa46,
           47:	pessoa47,
           48:	pessoa48,
           49:	pessoa49,
           50:	pessoa50}

soma = 0
count_m = 0
count_f = 0
alturas = []
for i in range(1, len(pessoas)):
    alturas.append(pessoas[i]['altura'])

    if (pessoas[i]['sexo'] == 'M'):
        soma += pessoas[i]['altura']
        count_m += 1
    else:
        count_f += 1

media = soma/count_m

print(f'Maior altura: {maior(alturas)}')
print(f'Menor altura: {menor(alturas)}')

print(f'Media da altura das mulheres: {media}')

print(f'Quantidade de homens: {count_f}')

print(f'Porcentagem de homens: {porcentagem(count_f, alturas):.2f}')
print(f'Porcentagem de mulheres: {porcentagem(count_m, alturas):.2f}')
