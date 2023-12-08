# Leitura dos valores de X e Y
X, Y = map(int, input().split())

# Inicialização da variável de contagem
count = 0

# Loop de 1 até Y
for i in range(1, Y + 1):
    # Imprime o número seguido de um espaço em branco
    print(i, end=" ")

    # Incrementa a contagem
    count += 1

    # Verifica se atingiu o valor de X para quebrar a linha
    if count == X:
        # Reinicia a contagem
        count = 0
        # Quebra a linha
        print()

    
