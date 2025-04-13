soma = 0
for i in range (0,6):
    x = int(input(f'Número {i+1}: '))
    
    if x % 2 == 0:
        soma += x

print(f'A soma dos pares é: {soma}') 