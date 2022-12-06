#  Número primo é aquele que só é divisível por ele mesmo e pela unidade. Fazer um algoritmo que determine e escreva os números primos compreendidos entre um intervalo fornecido pelo usuário.

def primo(n):
    for i in range(1, n):
        if i == 1:
            print(i)
            continue
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
        if primo:
            print(i)


primo(1000)
