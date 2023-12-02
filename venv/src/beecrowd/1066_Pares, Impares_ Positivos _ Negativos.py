par = 0
impar = 0
n = 0
p = 0
for i in range(5):
    enter = int(input())
    if enter % 2 == 0:
        par += 1
    else:
        impar +=1
    if enter > 0:
        p += 1
    elif enter < 0:
        n +=1 

print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{p} valor(es) positivo(s)')
print(f'{n} valor(es) negativo(s)')
