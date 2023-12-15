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

for l in range(tam):
    if l <= 5:
        for c in range(tam - l, tam):
            m = matriz[l][c]
            sup.append(m)
    else:
        for c in range(l+1,tam):
            m = matriz[l][c]
            sup.append(m)

       
soma = sum(sup)
media = soma / len(sup)

if op == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{media:.1f}')