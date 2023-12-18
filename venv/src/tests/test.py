def construir_matriz(ordem):
  """
  Constrói uma matriz de escada de ordem n.

  Args:
    n: Ordem da matriz.

  Returns:
    Uma matriz de escada de ordem n.
  """

  if ordem == 0:
    return []

  matriz = [[0 for _ in range(ordem)] for _ in range(ordem)]

  for i in range(ordem):
    for j in range(ordem):
      if i <= j:
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


if __name__ == "__main__":
  main()