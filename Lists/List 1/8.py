#Sortear dois numeros aleatórios a e b de 1 a 109 (incluindo 109) e mostrar o valor da multiplicação entre a e b. 

import random as rd

a = rd.randint(1, 109)
b = rd.randint(1, 109)

print(f'{a}*{b} = {a*b}')