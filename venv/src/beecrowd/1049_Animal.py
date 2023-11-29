def menu():
   animal = []
   for i in range(3):
        enter = input()
        animal.append(enter)
   return animal


def animal_genus(animal):

    if animal[0] == 'vertebrado':
        if animal[1] == 'ave':
            if animal[2] == 'carnivoro':
                print('aguia')
            else:
                print('pomba')
        else:
            if animal[2] == 'onivoro':
                print('homem')
            else:
                print('vaca')
    else:
        if animal[1] == 'inseto':
            if animal[2] == 'hematofago':
                print('pulga')
            else:
                print('lagarta')
        else:
            if animal[2] == 'hematofago':
                print('sanguessuga')
            else:
                print('minhoca')

enter = menu()
animal_genus(enter)    

