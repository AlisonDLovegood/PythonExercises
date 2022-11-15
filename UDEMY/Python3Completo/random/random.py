# por padrao os argumentos nao nomeados são separados por um espaço, a ferramenta sep serve para mudar isso
# o end serve para mudar o final da linha, normalmente hide
print(12, 34, sep=",", end='\n')
print(12, 34, sep=",")

# -----------------------------------------------------------------------------------------
a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)
