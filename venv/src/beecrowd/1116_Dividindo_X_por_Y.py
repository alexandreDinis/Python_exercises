n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    if y == 0:
        print('divisao impossivel')
    elif x == 0:
        break
    else:
        res = x / y
        print(f'{res:.1f}')
