from datetime import datetime

year = datetime.today().year

birth = int(input('Insira o ano do seu nascimento: '))
enlist = birth + 18
date = enlist - year
datep = abs(date)

if date > 0:
    print('Sua data de alistamento é: {} faltam {} anos'.format(enlist,datep))
else:
    print('Sua data de alistamento foi: {} passaram - se {} anos'.format(enlist,datep))




