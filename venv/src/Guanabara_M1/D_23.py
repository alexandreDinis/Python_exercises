number = input()
valores = ['unidade', 'dezenas', 'centenas', 'milhares']
number_cont = ['1','10','100','1000']
result = []
for i in range(4):
     r = int(number) // int(number_cont[i]) % 10
     result.append(r)
for i in range(4):        
   print(f'{valores[i]} {str(result[i])}')


