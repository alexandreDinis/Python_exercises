op_linha = int(input())
operacao = input()

matriz = []

for l in range(12):
    linha = []
    for c in range(12):
        n = float(input())
        linha.append(n)
    matriz.append(linha)

linha_escolhida = matriz[op_linha]
soma = sum(linha_escolhida)
media = soma / len(linha_escolhida)

if operacao == 'S':
    print(f'{soma:.1f}')
elif operacao == 'M':
    print(f'{media:.1f}')