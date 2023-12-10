n = int(input())

res = n
fat = []

for i in range(n,0,-1):
    fat.append(i)

for i in range(1,n):
    res *=  fat[i] 

print(res)



