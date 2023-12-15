op =  input()

matriz = []
tam = 12

for i in range(tam):
    linha = []
    for j in range(tam):
        n = float(input())
        linha.append(n)
    matriz.append(linha)

sub = []

for i in range(tam-1):
    for j in range(j+1):
        s = matriz[i][j]
        sub.append(s)

soma = sum(sub)
media = soma / len(sub)

if op == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{media:.1f}')

    
    