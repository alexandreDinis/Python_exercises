
'''''
maior = 0
for i in range(6):
    n = int(input())
    if n > maior:
        pos = i
        maior = n
print('{}\n{}'.format(maior,pos+1))
'''
numbers = []
for i in range(6):
    n = int(input())
    numbers.append(n)

maior = max(numbers)
position = numbers.index(maior)

print('{}\n{}'.format(maior,position+1))