import random as rd
from time import sleep
x = rd.randint(0,5)
a = -1
t = 0

print('---' * 20)
print('Vou pensar em um número de 1 a 5 tente adivinhar')
print('---' * 20)
print('Thinking')
print('---' * 20)

sleep(2)
print('Pensei pode tentar acertar')
print('---' * 20)

while a != x:
    a = int(input('Escolha um número: '))
    t += 1

print(f'Vc acertou o numero ({x}) em ({t}) tentativas')
    