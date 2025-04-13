words = ('Processamento', 'Informaçao', 'Karine')

for c in range(0, len(words)):
    vogais = 0
    palavra = words[c]
    for letra in palavra:
        if letra.lower() in 'aeiou':
            vogais += 1
    print(f'Na palavra {words[c]} temos {vogais} vogal(is)')
    
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra)
    
    