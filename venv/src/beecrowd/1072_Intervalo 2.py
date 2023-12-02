n = int(input())

inn = 0
out = 0
for i in range(n):
    n = int(input())
    if n >= 10 and n <= 20:
        inn += 1
    else:
        out += 1

print(f'{inn} in')
print(f'{out} out')

    