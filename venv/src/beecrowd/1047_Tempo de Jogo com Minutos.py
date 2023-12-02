def menu():
    ite = 4
    enter = input()
    times = [int(x) for x in enter.split()[:ite]]
    return times


def game_times(times):
    
    mi=mf=time=0
    
    mi = times[1] + (times[0]*60) 
    mf = times[3] + (times[2]*60)

    time = mf - mi
    if time <=0:
        time += 24 * 60
    
    h = time // 60
    m = time % 60

    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))

enter = menu()
game_times(enter)


