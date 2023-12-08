
while True:
    x = int(input())
    if x == 0:
        break
    for i in range(x):
       
        if i < x-1:
            print(i+1,end=' ')
        else:
            print(i+1)
