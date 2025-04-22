valores = list()
for i in range(5):
    valores.append(int(input(f'Insira o {i+1}° valor: ')))

maior = menor = valores[0]
posimaior = posimenor = 0

for p in range(5):
    if valores[p] > maior:
        maior = valores[p]
        posimaior = p

    
    if valores[p] < menor:
        menor = valores[p]
        posimenor = p
        
print(f'\nO maior valor é: {maior} e está no índice ({posimaior}) \nO menor valor é: {menor} e está no índice ({posimenor})')