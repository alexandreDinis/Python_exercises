n = int(input())

for i in range(n):

    div = 0

    x = int(input())
    
    for l in range(1,x+1):
        if x % l == 0: 
            div += 1
        
    if div == 2:
        print(x,'eh primo')
    else:
        print(x,'nao eh primo')