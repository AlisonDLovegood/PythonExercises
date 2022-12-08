# O Departamento Estadual de Meteorologia te contratou para desenvolver um programa que leia um conjunto de 100 temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

lst = []
print('============================================')
print('MAIOR, MENOR E MÉDIA DE 100 TEMPERATURAS')
for _ in range(5):
    lst.append((float(input('Digite uma temperatura: '))))
print('--------------------------------------------')
print(f'Maior temperatuda: {max(lst)}')
print(f'Menor temperatura: {min(lst)}')
print(f'Media de temperaturas: {sum(lst)/len(lst)}')
