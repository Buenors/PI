def operacoes(x,y):
    sum = x + y
    
    sub = x - y
    
    mult = x * y 
    
    if y == 0:
        div = 'y não pode ser 0' 
    else:
        div = x / y
        
    return print((sum, sub, mult, div))

operacoes(10,2)
operacoes(200,0)