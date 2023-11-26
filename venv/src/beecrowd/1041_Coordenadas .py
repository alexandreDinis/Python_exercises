
def coordinate(points):

    if points[0] == 0 and points[1] == 0:
        return print('Origem')
    elif points[0] < 0 and points[1]< 0:
        return print('Q3')
    elif points[0] < 0 and points[1] > 0:
        return print('Q2')
    elif points[0] > 0 and points[1] < 0:
        return print('Q4')
    elif points[0] == 0 and points[1] != 0:
        return print('Eixo Y')
    elif points[0] != 0 and points[1] == 0:
        return print('Eixo X')
    else:
        return print('Q1')
    

points = [float(point) for point in input().split()]

coordinate(points)

