impar = []

n = int(input())

for _ in range(n):
    try:
        x,y = map(int,input().split())
    except EOFError:
        break

    cont = 0
    while True:
        
        if x % 2 != 0:
            impar.append(x)
            cont += 1
            x+=1
        else:
            x += 1

        if cont == y:
            res = sum(impar)
            print(res)
            impar.clear()
            break





        
