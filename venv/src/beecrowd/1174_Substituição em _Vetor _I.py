vetor = []
valores = []

for _ in range(11):

   
    valor = input()
  
         

    if valor == "" :
        valor = 1
    vetor.append(valor)

for v in vetor:
    valores.append(int(v))

vetor.clear()    

for v in valores:
    if v <= 0:
        v = 1
        vetor.append(v)
    else:
        vetor.append(v)

tam = len(vetor)
for i in range(tam):
    print(f'x[{i}] = {vetor[i]}')    