
n = int(input())
enter = input()
vetor = [int(x) for x in enter.split()[:n]]

menor = min(vetor)
index = vetor.index(menor)

print(f'Menor valor: {menor}\nPosicao: {index}')

    