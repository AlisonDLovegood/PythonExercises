#  Numa eleição existem três candidatos identificados pelos números 1, 2 e 3. Faça um algoritmo que compute o resultado de uma eleição. Inicialmente o programa deve pedir o número total de votantes. Em seguida, deve pedir para cada votante votar (informando o numero do candidato) e ao final mostrar o número de votos de cada candidato.
def countl(votes, x):
    count = 0
    for i in range(len(votes)):
        if (votes[i] == x):
            count += 1
    return count


votes = []
qtd = int(input())
for i in range(qtd):
    votes.append(input())

print('O candidato 1 recebeu: {}'.format(countl(votes, '1')))
print('O candidato 2 recebeu: {}'.format(countl(votes, '2')))
print('O candidato 3 recebeu: {}'.format(countl(votes, '3')))
