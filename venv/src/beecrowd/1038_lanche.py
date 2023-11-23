enter = input().split()

cod  = int(enter[0])
qtdd = int(enter[1])

if cod == 1:
    total = qtdd * 4.0
elif cod == 2:
    total = qtdd * 4.5
elif cod == 3:
    total = qtdd * 5.0
elif cod == 4:
    total = qtdd * 2.0
elif cod == 5:
    total = qtdd * 1.5

print("Total: R$ %.2f"%total)
