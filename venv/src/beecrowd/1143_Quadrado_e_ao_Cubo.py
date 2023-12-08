n = int(input())
l = 1
for i in range(1,n+1):
    print(f'{i} ',end='')
    l = i ** 2
    print(f'{l} ',end='') 
    l = i ** 3
    print(f'{l}')

    print(f'{i} ',end='')
    l = i ** 2 +1
    print(f'{l} ',end='') 
    l = i ** 3 +1
    print(f'{l}')