from math import sin, cos, tan, radians
num = int(input('Digite o ângulo: '))
seno = sin(radians(num))
coseno = cos(radians(num))
tangente = tan(radians(num))
print(f'O seno é {seno:.2f}, o cosseno é {coseno:.2f} e a tangente é {tangente:.2f}')