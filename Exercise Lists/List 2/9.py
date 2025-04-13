def longestname(x):
    mais_longo = max(x, key=len)
    return print(f'O nome mais longo é: {mais_longo}')
        
        
longestname(['Carlos','Claudinei','Roberto'])       