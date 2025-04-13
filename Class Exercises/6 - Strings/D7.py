word = input('Insira a palavra: ')

if word == 'banana':
    print('a palavra é igual')
    
elif word < 'banana':
    print(f'A palavra {word} vem antes de banana na ordem alfabética')
    
elif word > 'banana':
    print(f'A palavra {word} vem depois de banana na ordem alfabética')