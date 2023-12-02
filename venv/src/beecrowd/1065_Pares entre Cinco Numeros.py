cont = 0 
for i in range(5):
    enter = int(input())
    if enter % 2 == 0:
        cont +=1
print(f'{cont} valores pares')