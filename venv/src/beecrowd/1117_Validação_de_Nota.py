cont = 0
nota = 0
notas = []

while True:
   
    nota = float(input())
    cont_nota = 0
    if nota < 0 or nota > 10:
        print('nota invalida') 
    else:
        notas.append(nota)
        cont +=1
        if cont == 2:
            media = sum((notas)) / cont
            print(f'media = {media:.2f}')
            break