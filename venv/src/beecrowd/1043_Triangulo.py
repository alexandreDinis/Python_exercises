
def perimeter_calculator(list):
   
    perimeter = sum(list)

    return perimeter


def trapeze_calculator(list):
    
    area = ((list[0] + list[1]) * list[2]) / 2

    return area

def analizator(list):
    
    if list[0] + list[1] > list[2] and list[1] + list[2] > list[0] and list[2] + list[0] > list[1]: 
        return True
    

def menu():
   
    iter  = 3
    enter = input()
    list  = [float(x) for x in enter.split()[:iter]]

    return list


list = menu()

analiza = analizator(list)

if analiza:
    result = perimeter_calculator(list)
    print('Perimetro = %.1f'%result)
else:
    result = trapeze_calculator(list)
    print('Area = %.1f'%result)



    



