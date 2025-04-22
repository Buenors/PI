matriz = [[0 for x in range(3)] for x in range(3)]

for l in range(3):
    for c in range(3):            
        matriz[l][c] = int(input(f'Insira o número pra posição [{l},{c}] da matriz 3x3: '))


y = int(input('Número a verificar se está na matriz: '))             

achou = False 
   
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if matriz[l][c] == y:
            print(f'Está na matriz na posição [{l},{c}]')
            achou = True
if not achou:
    print(f' O número {y} não está na matriz')
    
print('\nMatriz final:')
for linha in matriz:
    print(linha)


            
