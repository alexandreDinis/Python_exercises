second = 0
card   = 0
cards  = []
cards2 = []


def insart():
    print('-'*30)
    while True:
        card = input('Enter cards = ')
        
        if card == '0':
            break
        else:    
            cards.append(card)
    print(cards)        



def del_move():
    global cards
    global cards2
    global second
    
    print('-'*30)
    while True:
        op = 0
        second = 0
        cards2.clear()
        op = input('Enter [1] delete [-1] exit ')
        
        if op == '-1':
            break
        else:
            second = cards[1]
            cards.remove(second)
            del cards[0]
            for c in cards:
                cards2.append(c)
            cards2.append(second)
            print(cards2)
            
        cards.clear()
        for c in cards2:
            cards.append(c)

        print('')


print('')
insart()
del_move()

   
    



