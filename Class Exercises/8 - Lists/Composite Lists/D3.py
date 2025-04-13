def irreg(x):
    result = ''
    for i , p in enumerate(x):
        result += (f'Linha {i} tem {len(p)} elementos\n')   
        
    print(result)

        
irreg([[1,2,3],['f',1,2,4]])