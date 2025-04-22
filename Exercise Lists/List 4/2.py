numeros = list()

for i in range(5):
    valor = int(input(f'Digite o {i+1}° valor: '))
    
    if i == 0 or valor > numeros[-1]:
        numeros.append(valor)  # Adiciona no final se for o maior
    else:
        pos = 0
        while pos < len(numeros):
            if valor <= numeros[pos]:
                numeros.insert(pos, valor)  # Insere na posição correta
                break
            pos += 1

print(f'\nLista ordenada: {numeros}')