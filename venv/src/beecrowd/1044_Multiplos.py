def menu():

    iter = 2
    enter = input()
    menu = [int(x) for x in enter.split()[:iter]]

    return menu


def multiple(enter):
    
    orden = sorted(enter)
    resul = orden[1] % orden[0]
    if resul == 0:
        return True
    else:
        return False


enter = menu()

result = multiple(enter)

if result:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')

   