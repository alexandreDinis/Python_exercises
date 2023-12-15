op = input()

matriz = []
tam = 12

for l in range(tam):
    linha = []
    for c in range(tam):
        n = float(input())
        linha.append(n)
    matriz.append(linha)

sup = []

for l in range(6,tam):
    for c in range(11 -l +1,l):

        m = matriz[l][c]
        sup.append(m)

soma = sum(sup)
media = soma / len(sup)

if op == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{media:.1f}')