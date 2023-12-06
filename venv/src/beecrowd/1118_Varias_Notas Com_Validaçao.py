cont = 0
nota = 0
notas = []

vali = 1
while True:

    
    nota = float(input())
    if nota < 0 or nota > 10:
        print('nota invalida')
    else:
        notas.append(nota)
        cont +=1
        
        if cont == 2:
            media = sum((notas)) / cont
            print(f'media = {media:.2f}')
            notas.clear()
            print('novo calculo (1-sim 2-nao)')
            vali = int(input())
                    
            if vali == 1:
                cont = 0
                notas.clear()
                vali = 0
            elif vali == 2:
                break
            else:
                cont = 0
                notas.clear()
                while vali != 1 and vali != 2:
                    print('novo calculo (1-sim 2-nao)')
                    vali = int(input())

                        
                                



                
                        


            