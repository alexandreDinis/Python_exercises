cont =0
numbers = []
for i in range(6):
    enter = float(input())
    if enter > 0:
        cont += 1
        numbers.append(enter)

result = 0
for n in numbers:
  result += float(n) / cont

print(f'{cont} valores positivos')
print('{:.1f}'.format(float(result)))
