#Pegue o valor do imovel, o valor do salario, a quantidade de prestaçao
#O valor da prestaçao nao pode passar de 30% do salario 

imovel = float(input('Digite o valor do imovel: '))
salario = float(input('Digite o seu salario: '))
anos = int(input('Digite em quantas veses quer pagar: '))

parcela = imovel / (anos * 12)
comparador = salario * 0.30

print('Valor do imovel  = {:.2f}'.format(imovel))
print('valor da parcela = {:.2f}'.format(parcela))
print('quantidade de parcela = {}'.format(anos *12))

if parcela > comparador:
    print('Emprestimo Negado')
else:
    print('Emprestimo Aprovado') 
