name = input()

print(f'name = {name}')
print(f'maiuscula = {name.upper()}')
print(f'minuscula = {name.lower()}')

def contar_letras(name):
    return len(name) - name.count(' ')
cont = contar_letras(name)

print(f'numero de letras = {cont}')

names = [] 
names = name.split()

cont = len(names[0])

print(f'numeros de letras do prumeiro nome = {cont}')



