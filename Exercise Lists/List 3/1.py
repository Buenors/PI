w = str(input('Palavra que você deseja verificar se é um palíndromo: '))
wl = w.lower()
if wl == wl[::-1]:
    print(f'A palavra {w} é um palíndromo')

else:
    print(f'A palavra {w} não é um palíndromo')