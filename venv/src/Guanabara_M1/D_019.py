import random

studants = []

for i in range(0,4):
    n = input('Enter name = ')
    studants.append(n)

studant = random.choice(studants)

print(f'Studant = {studant}')


studants_sort = []

random.shuffle(studants)

print(f'Studants sorted = {studants}')
        



 
    
   