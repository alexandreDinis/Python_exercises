
n = float(input())

vetor = []
vetor.append(n)

for i in range(99):

    vetor.append(vetor[i] / 2)

for i,v in enumerate(vetor):

    print(f'N[{i}] = {v:.4f}')