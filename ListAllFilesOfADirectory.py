import os
pasta = '/Users\Aliso\Desktop\delnatur'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        print(os.path.join(diretorio, arquivo))
