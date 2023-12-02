cont = 0
enter = int(input())
if enter >= 0:
    if enter % 2 == 0:
        enter += 1
    for i in range(12):
        if enter % 2 == 0:
            enter += 1 
        else:
            print(enter)
            enter += 1