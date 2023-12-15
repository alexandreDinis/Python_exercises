tam = 12
matriz = []

for i in range(tam):
    linha = []
    for j in range(tam):
        linha.append('1')
    matriz.append(linha)


for l in range(tam):
        for c in range(l+1,tam):
            m = matriz[l][c]
            matriz[l][c] = "*"
       

for i in range(tam):
    for j in range(tam ):
        print(f'{matriz[i][j]}',end=' ')
    print()
