def income_tax(salary):

    if salary >=0 and salary <= 2000:
        print('Isento')
    elif salary >2000 and salary <= 3000:
        res = (salary - 2000) * 0.08
        print('R$ {:.2f}'.format(res))
    elif salary > 3000 and salary <= 4500:
        res = (salary - 3000) * 0.18 + ( 1000 * 0.08)
        print('R$ {:.2f}'.format(res))
    else:
        res = (salary - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
        print('R$ {:.2f}'.format(res))
    

enter = float(input())
income_tax(enter)
        

            
            
