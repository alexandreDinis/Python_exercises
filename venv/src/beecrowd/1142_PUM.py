n = int(input())
cont = 0
l = 1
for i in range(1,n+1):
    print(f'{l} ',end='')
    l += 1 
    print(f'{l} ',end='') 
    l += 1
    print(f'{l} ',end='')
    l += 1
    print('PUM')
    l += 1 
    if cont == 3:
        cont = 0
    
