""" 
    Fazer um algoritmo que:
        • Leia um número indeterminado de linhas contendo cada uma a idade de um indivíduo.
        • A última linha que não entrará nos cálculos, contém o valor da idade igual a zero.
        • Calcule e escreva a idade média deste grupo de indivíduos.
        • Escreva também a maior idade e a menor
"""
ages = []
while True:
    x = int(input())
    if x == 0:
        break
    else:
        ages.append(x)

# fazendo de modo puro
soma, mini, maxi = 0, 110, 0
for i in range(len(ages)):
    soma += ages[i]
    if mini > ages[i]:
        mini = ages[i]
    if maxi < ages[i]:
        maxi = ages[i]

avg = soma/len(ages)
print(f"media: {avg:,.2f}\nmaximo: {maxi}\nminimo: {mini}")
