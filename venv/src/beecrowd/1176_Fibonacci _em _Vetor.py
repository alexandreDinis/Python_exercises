n = int(input())

for _ in range(n):

    fib = [0, 1]

    m = int(input())

    if m == 0:
        print(f'Fib(0) = {0}')
    else:

        while len(fib) <= m:
            
            fib.append(fib[-1] + fib[-2])
            
        valor = fib[m] 
        indici = len(fib) -1   

        print(f'Fib({indici}) = {valor}')
