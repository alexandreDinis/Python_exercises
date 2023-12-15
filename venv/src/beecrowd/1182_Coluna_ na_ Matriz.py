read_colun = int(input())

option = input()

matriz = []
coluna = []
tam = 3

for l in range(tam):
    linha = []
    for c in range(tam):
        n = float(input())
        linha.append(n)
    matriz.append(linha)

for c in range(tam):
     colun = matriz[c][read_colun]
     coluna.append(colun)


soma = sum(coluna)
media = soma / len(coluna)

if option == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{media:.1f}')