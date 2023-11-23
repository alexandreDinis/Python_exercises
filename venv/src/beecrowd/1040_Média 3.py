#2 + 3 + 4 + 1

enter = input().split()

n1 = float(enter[0])
n2 = float(enter[1])
n3 = float(enter[2])
n4 = float(enter[3])

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4)  / 10

print('Media: %.1f'%media)

if media >= 7:
    print('Aluno aprovado.')
elif media  >= 5.0 and media <= 6.9:
    print('Aluno em exame.')
    n5 = float(input())
    print('Nota do exame: %.1f'% n5)    
    media = (media + n5) / 2
    if media >= 5:
        print('Aluno aprovado.')
        print('Media final: %.1f'% media)
    else:
        print('Aluno reprovado.')
        print('Media final: %.1f'% media)
else:
    print('Aluno reprovado.')






