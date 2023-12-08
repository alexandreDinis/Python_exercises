valores = input().split()
a = int(valores[0])
n = int(valores[len(valores)-1])
res = 0

for i in range(n):
    
    res += a + i

print(res)

