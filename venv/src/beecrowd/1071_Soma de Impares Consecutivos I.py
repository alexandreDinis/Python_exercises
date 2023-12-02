x = int(input())
y = int(input())

if x == y == 0:
    print(0)

if x > y:
    des = x
    x = y
    y = des

cont = 0   
for i in range(x+1,y):
    if i % 2 != 0:
        cont += i
print(cont)
    


   