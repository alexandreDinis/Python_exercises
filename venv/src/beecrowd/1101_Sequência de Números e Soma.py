while True:
    num = []
    ite = 2
    soma = 0
    enter = input()
    numbers = [int(x) for x in enter.split()[:ite]]
    
    if numbers[1] <=0 or numbers[0] <= 0:
        break
    else:
        numbers.sort()
        ini = numbers[0]
        fim = numbers[1]
        for i in range(ini,fim+1):
            num.append(i)
            soma += i
    
        print(*num, end=' ')
        print('Sum={}'.format(soma))            
        
