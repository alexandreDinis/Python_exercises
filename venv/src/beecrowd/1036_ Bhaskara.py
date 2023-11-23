

enter = input().split()

a = float(enter[0])
b = float(enter[1])
c = float(enter[2])

delta = b * b - 4 * a * c

if a == 0 or delta < 0 :
    print('Impossivel calcular')
else:
    x1 = (-b + (delta**(1/2)))/ (2*a)
    x2 = (-b - (delta**(1/2)))/ (2*a)

    print("R1 = %.5f"%x1)
    print("R2 = %.5f"%x2)






