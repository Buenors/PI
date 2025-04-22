expressao =  input('Digie a expressão com parênteses: ')
verif = list()

for caractere in expressao:
    if caractere == '(':
        verif.append('(')
        
    elif caractere == ')':
        
        if len(verif) > 0:
            verif.pop()
            
        else:
            erro = True
            verif.append(')')

if not erro and len(verif) == 0:
    print('A expressão está com os parênteses corretos')
    
else:
    print('A expressão não está com os parênteses corretos')