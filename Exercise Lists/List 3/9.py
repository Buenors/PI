def nomemaislongo(x):
    maislongo = ""
    maior_len = 0
    
    for name in x:
        if len(name) > maior_len:
            maislongo = name
            maior_len = len(name)
            
    return print(f'O nome mais longo é: {maislongo}, com ({maior_len}) caracteres')
        
nomemaislongo(('Jose','Claudinei Carlos Abobrinha','Jeregotango da silva'))       