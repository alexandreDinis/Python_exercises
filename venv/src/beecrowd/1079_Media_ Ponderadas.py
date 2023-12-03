notas = []
peso = [2,3,5]
n = int(input())
for i in range(n):
    enter = input()
    notas = [float(x) for x in enter.split()[:3]]
    media = sum([notas * peso for notas,peso in zip(notas,peso)]) / sum(peso)
    print('{:.1f}'.format(media))
