import math

# x = (-b ± √(b² - 4ac)) / 2a  

a = float(input(''))
b = float(input(''))
c = float(input(''))
    
delta = pow(b,2) - (4 * a * c)

if delta < 0 or a == 0 or b == 0 or c == 0:
    print('Impossivel calcular\n')
else:  
    sqrt = math.sqrt(delta)
    x1 = (-b + sqrt) / (2 * a)
    x2 = (-b - sqrt) / (2 * a)
    
    print(f'R1 = {x1:.5f}\nR2 = {x2:.5f}\n')





