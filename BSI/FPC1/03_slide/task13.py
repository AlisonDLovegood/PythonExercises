# Desenvolva um algoritmo que efetue a leitura de três valores numéricos representando os lados de um triângulo. O algoritmo deverá verificar e informar se os lados fornecidos formam realmente um triângulo (cada lado é menor que a soma dos outros dois lados). Se esta condição for verdadeira, deverá ser indicado qual tipo de triângulo foi formado: isósceles (dois lados iguais e um diferente), escaleno (todos os lados diferentes) ou eqüilátero (todos os lados são iguais).

l1 = int(input())
l2 = int(input())
l3 = int(input())
if l2+l3 > l1 and l1+l3 > l2 and l1+l2 > l3:
    print('Forma um triangulo: True')
    if (l1 == l2) or (l1 == l3) or (l3 == l2):
        print('Tipo do triangulo: Isósceles')
    elif (l1 != l2) and (l1 != l3) and (l3 != l2):
        print('Tipo do triangulo: Escaleno')
    else:
        print('Tipo do triangulo: Equilátero')
else:
    print("Forma um triangulo: False")
