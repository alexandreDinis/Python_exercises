n = int(input())
org = 0
cont = 0
for i in range(n):
    a,b = map(int,input().split())

    if a > b:
        org = a
        a = b
        b = org

    for i in range(a+1,b):

        if i % 2 != 0:
            cont +=i

    print(cont)
    cont = 0

