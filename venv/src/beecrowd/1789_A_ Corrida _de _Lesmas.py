
while True:
    try:
        n = int(input())

        lesmas = [int(x) for x in input().split()[:n]]
        
    except EOFError:
        break

    res = max(lesmas)

    if res < 10:
        print('1')
    elif res >= 10 and res < 20:
        print('2')
    else:
        print('3')