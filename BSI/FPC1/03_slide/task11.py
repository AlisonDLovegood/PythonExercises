print('---------------------------------------------------------')
print('------ DIGITE UM NÚMERO PARA SER FEITO SUA TABUADA ------')
n = int(input())

for i in range(1, n+1):
    print('---------------------------------------------------------')
    print(f'---------------------- TABUADA DO {i} ---------------------')
    print('--- ADIÇÃO ---')
    for j in range(1, 10):
        print(f'{i}+{j} = {i+j}')
    print('--- SUBTRAÇÃO ---')
    for j in range(1, 10):
        print(f'{i}-{j} = {i-j}')
    print('--- MULTIPLICAÇÃO ---')
    for j in range(1, 10):
        print(f'{i}*{j} = {i*j}')
    print('--- DIVISÃO ---')
    for j in range(1, 10):
        print(f'{i}/{j} = {i/j}')
