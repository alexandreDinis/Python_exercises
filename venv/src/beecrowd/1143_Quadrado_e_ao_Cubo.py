n = int(input())
l = 1
for i in range(1,3):
    print(f'{i} ',end='')
    l = i ** 2
    print(f'{l} ',end='') 
    l = i ** 3
    print(f'{l}')
l = 2
for i in range(3,(n*2+1)):
    l  = i+1
    print(f'{l} ',end='')
    l  +=1
    print(f'{l} ',end='') 
    l = i
    print(f'{l}')
     