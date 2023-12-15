def construir_matriz(ordem):
    if ordem == 0:
        return []

    # A linha abaixo utiliza uma lista de compreensão para criar a matriz com base na ordem fornecida.
    # A expressão min(i, j, ordem-i-1, ordem-j-1) + 1 calcula o valor correspondente a cada posição da matriz,
    # de acordo com a lógica desejada.
    matriz = [[min(i, j, ordem-i-1, ordem-j-1) + 1 for j in range(ordem)] for i in range(ordem)]
    return matriz

# Este é um loop infinito que solicita entrada do usuário até que o valor inserido seja zero.
while True:
    # Converte a entrada do usuário para um número inteiro.
    ordem = int(input())
    
    # Se a ordem for zero, encerra o loop.
    if ordem == 0:
        break

    # Chama a função construir_matriz para criar a matriz com base na ordem fornecida.
    matriz = construir_matriz(ordem)

    # Itera sobre cada linha da matriz e imprime os valores formatados conforme as especificações.
    for linha in matriz:
        # A expressão " ".join(f"{valor:2}" for valor in linha) cria uma string formatada
        # para cada valor na linha, com um campo de tamanho 2 justificado à direita.
        # Essas strings são então concatenadas com espaços entre elas.
        print(" ".join(f"{valor:2}" for valor in linha))
    
    # Imprime uma linha em branco após a matriz.
    print()
