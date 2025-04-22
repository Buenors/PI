matriz = [[],[]]
for i in range(7):
    x = int(input(f'Insira o {i+1}º número: '))
    if x % 2 == 0:
        matriz[0].append(x)
        
    else:
        matriz[1].append(x)
matriz[0].sort()
matriz[1].sort()        

print(f'\nPares: {matriz[0]} \nÍmpares: {matriz[1]}')