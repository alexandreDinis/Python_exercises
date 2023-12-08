cont = 0

x,y = map(int,input().split())

for i in range(y):
    cont+=1
    if cont == x:
        print(i+1 ,end='\n')
        cont = 0
    else:
        print(i+1,end=' ')