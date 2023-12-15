vetor = []

for _ in range(100):

    n = float(input())

    vetor.append(n)

for i,v in enumerate(vetor):
    if v <= 10:
        print(f'A[{i}] = {vetor[i]}')
