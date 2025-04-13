w = str(input('Palavra que você quer fazer a "escada": '))

for i in range(0, len(w)):
    print(w[:i+1])