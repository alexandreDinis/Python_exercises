while True:
    try:
        entrada = int(input())

    except EOFError:
        break

    if entrada  <= 0:
        print('vai ter copa!')
    else:
        print('vai ter duas!')


      