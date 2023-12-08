def contar_diamante(enter):
    pilha = []
    diamante = 0

    for caracter in enter:
        if caracter == "<":
            pilha.append(caracter)
        elif caracter == ">" and pilha:
            diamante +=1
            pilha.pop()

    return diamante

num_casos = int(input())

for _ in range(num_casos):
    enter = input()
    resultado = contar_diamante(enter)
    print(resultado)

