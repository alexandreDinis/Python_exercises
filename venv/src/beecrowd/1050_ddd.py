ddd = {'11': 'Sao Paulo', '61': 'Brasilia','71': 'Salvador','21': 'Rio de Janeiro',
       '32': 'Juiz de Fora','19': 'Campinas','27': 'Vitoria', '31': 'Belo Horizonte'}


enter = input()

if enter in ddd:
    result = ddd[enter]
    print(result)
else:
    print('DDD nao cadastrado')
