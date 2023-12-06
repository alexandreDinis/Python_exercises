a = int(input())
b = int(input())
cont = 0

if a > b:
    c = a
    a = b
    b = c

for i in range(a,b+1):
    if i % 13 != 0:
        cont += i
print(cont)

    