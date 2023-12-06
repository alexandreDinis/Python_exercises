i = 0
j = 1

while i <= 2:
    for l in range(3):
        if i != int(i):
            print('I={:.1f} J={:.1f}'.format(i,j))
        else:
            print(f'I={i:.0f} J={j:.0f}')
        j +=1
    j = round(j - 2.8, 1)
    i = round(i + 0.2, 1)
    
    