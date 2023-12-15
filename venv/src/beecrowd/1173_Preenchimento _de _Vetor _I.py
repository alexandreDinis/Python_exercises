vetor = []

n = int(input())

vetor.append(n)

for i in range(9):

    vetor.append(vetor[-1] * 2) 

for i in range(len(vetor)):
    print(f'N[{i}] = {vetor[i]}')