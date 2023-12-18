n = int(input())
cont = 0
papel = ['pedra','Spock']
tesoura = ['papel', 'lagarto']
pedra = ['lagarto', 'tesoura']
spok = ['tesoura', 'pedra']
lagarto = ['Spock', 'papel']

while cont != n:

    casos = [str(x) for x in input().split()[:2]]

    if casos[0] == casos[1]:
        cont += 1 
        print(f'Caso #{cont}: De novo!')
    elif casos[0] == 'papel' and casos[1] in papel or casos[0] == 'tesoura' and casos[1] in tesoura or casos[0] == 'pedra' and casos[1] in pedra or casos[0] == 'lagarto' and casos[1] in lagarto or casos[0] == 'Spock' and casos[1] in spok:
        cont +=1
        print(f'Caso #{cont}: Bazinga!')
    else:
        cont +=1 
        print(f'Caso #{cont}: Raj trapaceou!')
    casos.clear()
    
   
    
