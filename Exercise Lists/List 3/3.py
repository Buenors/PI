f = str(input('Contar as vogais da frase: '))
f_lower = f.lower()
vogais = 0

for letter in f_lower:
    if letter.lower() in 'aeiou':
        vogais += 1
        
print(f'A frase({f}) tem {vogais} vogais')