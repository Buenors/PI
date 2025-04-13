n = int(input('Numero de itens no elevador: '))
i = 1
peso = 0

for i in range (n):
    p = int(input(f'Peso item {i+1}: '))
    peso += p
    
print(f'O peso total dos itens é: {peso}kg')
if p <= 420:
    print('S')
    
else:
    print('N')