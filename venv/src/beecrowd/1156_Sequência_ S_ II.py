soma = 1
seq = [0,1]
base = [0,1]

while len(seq) < 21:
    seq.append(seq[-1] + seq[-1])
    base.append(base[-1] + 2)

for i in range(2,21):
    soma += base[i] / seq[i]
    
print(f'{soma:.2f}')