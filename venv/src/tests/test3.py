tam =5
matriz = []

for i in range(tam):
    linha = []
    for j in range(tam):
        linha.append('1')
    matriz.append(linha)


for l in range(tam):
        for c in range(tam -i -1):
            m = matriz[l][c]
            matriz[l][c] = "*"
       

for i in range(tam):
    for j in range(tam ):
        print(f'{matriz[i][j]}',end=' ')
    print()
