banknotes  = [100, 50, 20, 10, 5, 2]
coins      = [1, 0.50, 0.25, 0.10, 0.05, 0.01]



list_notes = ['nota(s) de R$ 100.00','nota(s) de R$ 50.00','nota(s) de R$ 20.00','nota(s) de R$ 10.00',
              'nota(s) de R$ 5.00','nota(s) de R$ 2.00']

list_coins = ['moeda(s) de R$ 1.00','moeda(s) de R$ 0.50','moeda(s) de R$ 0.25','moeda(s) de R$ 0.10',
              'moeda(s) de R$ 0.05','moeda(s) de R$ 0.01']

notes_coins = [100, 50, 20, 10, 5, 2,1, 0.50, 0.25, 0.10, 0.05, 0.01]

list_coins_notes = ['nota(s) de R$ 100.00','nota(s) de R$ 50.00','nota(s) de R$ 20.00','nota(s) de R$ 10.00',
                    'nota(s) de R$ 5.00','nota(s) de R$ 2.00','moeda(s) de R$ 1.00','moeda(s) de R$ 0.50','moeda(s) de R$ 0.25',
                    'moeda(s) de R$ 0.10','moeda(s) de R$ 0.05','moeda(s) de R$ 0.01']


def div_money(n):
    n = int(n * 100)  # Converte para centavos (multiplica por 100)
    result_notes = []

    for value in notes_coins:
        result = n // int(value * 100)
        rest = n % int(value * 100)
        result_notes.append(result)
        n = rest

    return result_notes



def prints(l_result,l_str):
    
    print('NOTAS:')
    
    for i,l in zip(l_result,l_str):

        if l == 'moeda(s) de R$ 1.00':
            print('MOEDAS:')    
        print('%.0f'%i, l)


n = float(input())

result = div_money(n)
prints(result,list_coins_notes)




 


