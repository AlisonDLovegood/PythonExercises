# Anacleto tem 1,50m e cresce 2 centímetros por ano, enquanto Felisberto tem 1,10 e cresce 3 centímetros por ano. Construa um programa que calcule e apresente quantos anos serão necessários para que Felisberto seja maior que Anacleto.

anacleto = 1.5
felisberto = 1.1
count = 0
while felisberto < anacleto:
    anacleto += 0.02
    felisberto += 0.03
    count += 1

print(f'anos necessários: {count}')
print(f'altura de Anacleto: {anacleto:.2f}')
print(f'altura de Felisberto: {felisberto:.2f}')
