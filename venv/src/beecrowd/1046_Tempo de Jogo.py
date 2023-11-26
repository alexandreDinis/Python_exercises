def menu():
    ite = 2
    enter = input()
    times = [int(x) for x in enter.split()[:ite]]
    return times


def game_time(times):

    if times[0] == times[1]:
        print('O JOGO DUROU 24 HORA(S)')
    elif times[0] > times[1]:
        result = (24 - times[0]) + times[1]
        print('O JOGO DUROU {} HORA(S)'.format(result))
    else:
        result = times[1] - times[0]
        print('O JOGO DUROU {} HORA(S)'.format(result))    


enter_times = menu()
game_time(enter_times)