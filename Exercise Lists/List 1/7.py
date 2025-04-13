# Gerar um numero aleatório entre 1 e 100 e tentar adivinhar

import random as rd
# randrange (exclusivo) e randint (inclusivo)
c = input('Chute um número de 1 a 100 ')
r = rd.randint(1, 100)

if c == r:
    
    print(f'Você acertou o número ({r})')
    
else:
    
    print(f'Você errou o número era {r} \n Seu chute foi {c}')