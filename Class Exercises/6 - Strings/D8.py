def contagem(string, letter):
    cont = 0 
    for letra in string:
        if letra == letter:
            cont += 1
            
    print(cont)
    
contagem('arroz','a')
    