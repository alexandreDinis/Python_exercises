n = int(input())

for i in range(n):
    num = int(input())
    if num == 0:
        print('NULL')
    elif num < 0 and num % 2 == 0:
        print('EVEN NEGATIVE')
    elif num < 0 and num % 2 != 0:
        print('ODD NEGATIVE')
    elif num > 0 and num % 2 == 0:
        print('EVEN POSITIVE')
    else:
        print('ODD POSITIVE')