pares = []

while True:
    
    n = int(input())

    if n == 0:
        break

    while True:  

        if n % 2 == 0:
            pares.append(n)
            n+=1
        else:
            n+=1
        
        if len(pares) == 5:
            res = sum(pares)
            print(res)
            break

    pares.clear()
    
     
    

