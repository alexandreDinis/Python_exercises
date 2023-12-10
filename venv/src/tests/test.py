def crescimento_poulacao(valor,porcentagem):
    
    porcentagem = porcentagem / 100
    valor_porcentagem = valor * porcentagem
    valor_porcentagem = round(valor_porcentagem)

    return valor_porcentagem


t = int(input())

tempo = 0

for _ in range(t):
    pa,pb,g1,g2 = input().split()
    

con_pa = int(pa)
con_pb = int(pb)

while True:
     
    cidade_a = crescimento_poulacao(int(pa),float(g1))
    con_pa += cidade_a
    cidade_b = crescimento_poulacao(int(pb),float(g2))
    con_pb += cidade_b
    tempo += 1
        
    if cidade_b < cidade_a:
        print(f'{tempo} anos.')
        print(cidade_a,cidade_b)
        break
