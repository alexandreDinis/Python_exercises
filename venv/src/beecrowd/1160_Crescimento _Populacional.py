def crescimento_poulacao(valor,porcentagem):
    
    porcentagem = porcentagem / 100
    valor_porcentagem = valor * porcentagem
    valor_porcentagem = round(valor_porcentagem) /1

    return valor_porcentagem


t = int(input())

tempo = 0

for _ in range(t):
    
    pa,pb,g1,g2 = input().split()
    

    con_pa = int(pa)
    con_pb = int(pb)

    while True:
        
        tempo += 1
        cidade_a = crescimento_poulacao(con_pa,float(g1))
        con_pa += cidade_a
        cidade_b = crescimento_poulacao(int(con_pb),float(g2))
        con_pb += cidade_b
        
        if tempo > 100:
            print('Mais de 1 seculo.')
            break
        elif con_pa > con_pb:
            print(f'{tempo} anos.')
            break

    con_pa=con_pb=cidade_a=cidade_b=tempo=0


