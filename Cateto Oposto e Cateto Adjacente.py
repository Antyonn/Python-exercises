import math
opo = float(input('Digite o cateto oposto: '))
adj = float(input('Digite o cateto adjacente: '))
hip = math.hypot(opo, adj)
print(f'O comprimento da hipotenusa é: `{hip:.2f}')
