n = 0
alc = 0
gas = 0
dis = 0
comb = [1,2,3]
while n !=  comb:
    n = int(input())
    if n == 4:
        print(f'MUITO OBRIGADO\nAlcool: {alc}\nGasolina: {gas}\nDiesel: {dis}')
        break
    elif n ==1:
        alc += 1
    elif n == 2:
        gas += 1
    elif n == 3:
        dis += 1
    

