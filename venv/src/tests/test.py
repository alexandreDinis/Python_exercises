enter = input('digite os nomes')
nome = [str(x) for x in enter.split()[:4]]
n = str(input('digite o nome '))
if n in nome:
    print('nome maneiro')
else:
    print('nome comum')