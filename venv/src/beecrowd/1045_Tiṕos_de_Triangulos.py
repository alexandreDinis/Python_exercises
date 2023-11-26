def menu():
    
    ite = 3
    enter = input()
    m = [float(x) for x in enter.split()[:ite]]
    n = []
    for x in m:
        if x > 0:
            n.append(x)

    n_decr = sorted(n, reverse=True)

    return n_decr


def tipo_triangulo(lis):
    
    lista = []
    for x in lis:
        lista.append(float(x))
    
    if lista[0] >= (lista[1] + lista[2]):
        print('NAO FORMA TRIANGULO')
    else:    
        if pow(lista[0], 2) == pow(lista[1], 2) + pow(lista[2], 2):
            print('TRIANGULO RETANGULO')
        elif pow(lista[0], 2) > pow(lista[1], 2) + pow(lista[2], 2):
            print('TRIANGULO OBTUSANGULO')
        elif pow(lista[0], 2) < pow(lista[1], 2) + pow(lista[2], 2):
            print('TRIANGULO ACUTANGULO')
        if lista[0] == lista[1] == lista[2]:
            print('TRIANGULO EQUILATERO')
        elif lista[0] == lista[1] or lista[1] == lista[2]:
            print('TRIANGULO ISOSCELES')


enter = menu()
tipo_triangulo(enter)
    
