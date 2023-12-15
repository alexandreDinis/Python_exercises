def construir_matriz(n):
  """
  Constrói uma matriz de escada de ordem n.

  Args:
    n: Ordem da matriz.

  Returns:
    Uma matriz de escada de ordem n.
  """

  matriz = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(i + 1):
      matriz[i][j] = i + j

  return matriz


def main():
  """
  Lê a entrada e imprime as matrizes de escada.
  """

  n = int(input())
  while n != 0:
    matriz = construir_matriz(n)

    for linha in matriz:
      for elemento in linha:
        print(f"{elemento:3}", end=" ")
      print()
    print()

    n = int(input())
