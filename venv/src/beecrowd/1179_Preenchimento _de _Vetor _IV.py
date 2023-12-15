impar = []
par = []
cont_p = 0
cont_i = 0

for _ in range(15):

    n = int(input())

    if n % 2 == 0:
        par.append(n)
        cont_p += 1
        if cont_p == 5:
            for i,v in enumerate(par):
                 print(f'par[{i}] = {v}')
            par.clear()
            cont_p =0
    else:
        impar.append(n)
        cont_i += 1
        if cont_i == 5:
            for i,v in enumerate(impar):
                print(f'impar[{i}] = {v}')
            impar.clear()
            cont_i = 0

for i,v in enumerate(impar):
    print(f'impar[{i}] = {v}')

for i,v in enumerate(par):
    print(f'par[{i}] = {v}')
