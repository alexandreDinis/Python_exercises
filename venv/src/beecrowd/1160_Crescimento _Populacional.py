t = int(input())
for _ in range(0,t):

    enter = input().split()
    pa = int(enter[0])
    pb = int(enter[1])
    g1 = float(enter[2]) / 100
    g2 = float(enter[3]) / 100
    
    tempo = 0
    while True:

        pa += int(pa * g1)
        pb += int(pb * g2)
        tempo += 1 
        if pa > pb or tempo > 100:
            break

    if tempo <= 100:
        print(f'{tempo} anos.')
    else:
        print('Mais de 1 seculo.')
        
   


