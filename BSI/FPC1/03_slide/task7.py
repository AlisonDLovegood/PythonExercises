
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
