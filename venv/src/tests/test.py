n = int(input())
l = 1

for i in range(1, n * 4 +1):
    print(f'{l} ', end='' if i % 4 != 0 else 'PUM\n')
    l += 1 if i % 4 != 0 else 2