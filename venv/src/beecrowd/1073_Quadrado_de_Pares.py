n  = int(input())

for i in range (n+1):
    if i == 0:
        pass
    else:
        if i % 2 == 0:
            l = pow(i,2)
            print(f'{i}^2 = {l}')