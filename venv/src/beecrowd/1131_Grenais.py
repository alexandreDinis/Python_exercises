cont = 0
vit_inter = 0
vit_gremio = 0
empates = 0

while True:
    i,g = map(int,input().split())
    cont += 1
    if i > g:
        vit_inter += 1
    elif i < g:
        vit_gremio +=1
    else:
        empates += 1
    print('Novo grenal (1-sim 2-nao)')
    n = int(input())
    if n == 2:
        print(f'{cont} grenais\nInter:{vit_inter}\nGremio:{vit_gremio}\nEmpates:{empates}')
        if vit_gremio < vit_inter:
            print('Inter venceu mais')
        elif vit_gremio > vit_inter:
            print('Gremio venceu mais')
        else:
            print('Nao houve vencedor')
        break    



