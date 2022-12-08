# Faça o algoritmo de imprimir a tabuada de um número fornecido pelo usuário, usando while. Após mostrar a tabuada o programa deve perguntar se deseja imprimir a tabuada de um novo número.

while True:
    print('==============================================')
    print('REGRA: DIGITE 0 PARA FECHAR O PROGRAMA')
    n = int(input('DIGITE UM NÚMERO PARA APRESENTAR SUA TABUADA: '))
    i = 1
    if n == 0:
        break
    elif n < 10:
        print('----------------------------------------------')
        while i < 11:
            print(f'{n}*{i} = {i*n}')
            i += 1
    else:
        print('----------------------------------------------')
        while i <= n:
            print(f'{n}*{i} = {i*n}')
            i += 1
    print('----------------------------------------------')
