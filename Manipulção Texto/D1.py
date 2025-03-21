name = input("Insira seu nome: ")
nameup = name.upper()
namelow = name.lower()
namelen = len(name) - name.count(' ')

print(f'Nome maiúsculo: {nameup} \nNome minúsculo: {namelow} \nQuantidade de letras: {namelen}')
