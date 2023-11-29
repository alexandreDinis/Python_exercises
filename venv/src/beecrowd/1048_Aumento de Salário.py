def salary_adjustment(salary):
    
    if  salary >= 0 and salary <= 400:
        perc = 0.15
        res  =  perc * salary 
        new_salary = salary + res
        print('Novo salario: {:.2f}'.format(new_salary))
        print('Reajuste ganho: {:.2f}'.format(res))
        print('Em percentual: {:.0f} %'.format((perc * 100)))
    elif salary >= 400.01 and salary <= 800:
        perc = 0.12
        res  =  perc * salary 
        new_salary = salary + res
        print('Novo salario: {:.2f}'.format(new_salary))
        print('Reajuste ganho: {:.2f}'.format(res))
        print('Em percentual: {:.0f} %'.format((perc * 100)))
    elif salary >= 800.01 and salary <= 1200.00:
        perc = 0.10
        res  =  perc * salary 
        new_salary = salary + res
        print('Novo salario: {:.2f}'.format(new_salary))
        print('Reajuste ganho: {:.2f}'.format(res))
        print('Em percentual: {:.0f} %'.format((perc * 100)))
    elif salary >= 1200.01 and salary <= 2000.00:
        perc = 0.07
        res  =  perc * salary 
        new_salary = salary + res
        print('Novo salario: {:.2f}'.format(new_salary))
        print('Reajuste ganho: {:.2f}'.format(res))
        print('Em percentual: {:.0f} %'.format((perc * 100)))
    else:
        perc = 0.04
        res  =  perc * salary 
        new_salary = salary + res
        print('Novo salario: {:.2f}'.format(new_salary))
        print('Reajuste ganho: {:.2f}'.format(res))
        print('Em percentual: {:.0f} %'.format((perc * 100)))


salary = float(input())
salary_adjustment(salary)

