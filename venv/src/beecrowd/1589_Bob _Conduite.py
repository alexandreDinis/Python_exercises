n = int(input())

for _ in range(n):
    enter = input()
    n = [int(x) for x in enter.split()[:2]]

    res = sum(n)

    print(res)

