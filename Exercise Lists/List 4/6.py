matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapar = somaterceira = 0
for l in range(3):
    for c in range(3):  
        x = (int(input('Insira os números da matriz 3x3: ')))
        matriz[l][c] = x
        if x % 2 == 0:
            somapar += x
        
        if c == 2:
            somaterceira += x
            
maior_segundalinha = max(matriz[1])             
print(f'\nSoma dos pares: {somapar} \nSoma da terceira coluna: {somaterceira} \nO maior valor da segunda linha é: {maior_segundalinha}')