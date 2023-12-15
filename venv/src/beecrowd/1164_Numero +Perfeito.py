n = int(input())


for i in range(n):

    div = 0

    x = int(input())

    for l in range(1,x):

        if x % l == 0: 
            div += l
        
    if div == x:
        print(x,'eh perfeito')
    else:
        print(x,'nao eh perfeito')
        
               