vetor = []

n = int(input())

m = 0
cont = 0

while cont < 1000:

    if m > n-1:
        m = 0
    else:
        vetor.append(m)
        m +=1 
        cont += 1

for i,v in enumerate(vetor):

    print(f'N[{i}] = {v}')
        
