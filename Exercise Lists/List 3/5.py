numeros = tuple(float(input(f'Insira o {i+1}º número: ')) for i in range(4))


print(f'\nVocê digitou os valores: {numeros}')


print(f'O valor 9 apareceu {numeros.count(9)} vez(es).')

if 3 in numeros:
    print(f'O valor 3 foi digitado na {numeros.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')

pares = [n for n in numeros if n % 2 == 0]
if pares:
    print(f'Os números pares digitados foram: {pares}')
else:
    print('Nenhum número par foi digitado.')
    