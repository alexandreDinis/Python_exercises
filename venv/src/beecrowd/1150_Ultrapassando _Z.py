a = int(input())

while True:
    try:
        x = int(input())
    except EOFError:
        break
        
    if x > a:
        cont = 0
        soma = 0


    for i in range(a,x):

        soma += i
        cont += 1

        if soma > x:
            print(cont)
            break
