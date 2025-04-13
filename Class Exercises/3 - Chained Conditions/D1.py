import random as rd
from time import sleep
x = rd.randint(1,2)

print('---' * 20)
print('Vou pensar em um número de 1 a 5 tente adivinhar')
print('---' * 20)

a = int(input('Escolha um número: '))

print('...processing...')
sleep(2)

if a == x:
    print(f'Vc acertou ({x})')
    
else:
    
    print(f'VC errou o número era ({x})')