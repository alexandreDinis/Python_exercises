years = []
soma = 0

while True:
    try:
        n = int(input())
    except EOFError:
        break
    if n > 0:
        years.append(n)

    if n < 0:
        media = len(years) 
        soma = sum(years) / media
        print(f'{soma:.2f}')
        break