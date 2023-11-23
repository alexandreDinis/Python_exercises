
numb_neg  = []
numb_pos  = []
ordem_pos = []
ordem_neg = []
num_ordem = []


def simple_shorts(numbers):
    
    for number in numbers:
        if number < 0:
            numb_neg.append(number)
        else:
            numb_pos.append(number)
    ordem_pos = sorted(numb_pos)
    ordem_neg = sorted(numb_neg)

    for n in ordem_neg:
        if ordem_neg:
            num_ordem.append(n)
    for n in ordem_pos:
        if ordem_pos:
            num_ordem.append(n)
    for n in num_ordem:
        print(n)

    for number in numbers:
        print(number)
    print()


numbers = [int(x) for x in input().split()[:3]]
simple_shorts(numbers)


