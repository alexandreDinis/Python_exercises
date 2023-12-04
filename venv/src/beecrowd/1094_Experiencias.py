coelho =[]
sapo =[]
rato = []
n = int(input())
for i in range(n):
    n,c = input().split()
    if c == 'C':
        coelho.append(int(n))
    elif c == 'S':
        sapo.append(int(n))
    else:
        rato.append(int(n))
coelhos = sum(coelho)
ratos = sum(rato)
sapos = sum(sapo)
total = coelhos + sapos + ratos
perc_coelho = (coelhos / total) * 100
perc_rato = (ratos / total) * 100
perc_sapo = (sapos / total) * 100

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(coelhos))
print('Total de ratos: {}'.format(ratos))
print('Total de sapos: {}'.format(sapos))
print('Percentual de coelhos: {:.2f} %'.format(perc_coelho))
print('Percentual de ratos: {:.2f} %'.format(perc_rato))
print('Percentual de sapos: {:.2f} %'.format(perc_sapo))
