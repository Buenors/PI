maior = 0
menor = 0

for i in range(0, 5):
    peso = float(input(f'Peso da {i+1}ª pessoa (em kg): '))

    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'Maior peso lido: {maior} kg \nMenor peso lido: {menor} kg')