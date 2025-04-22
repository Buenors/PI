def comparaconsumo(x,y):
    somax = somay = 0  # x são os datacenters e y as familias
    comp = ''
    somax = sum(x)
        
    somay = sum(y)
        
    mediax = somax / len(x)
    mediay = somay / len(y)
    
    if mediax == mediay:
        comp = 'Ambos consomem a mesma quantidade de água em média'
   
    elif mediay > mediax:
        comp = 'As famílias consomem mais água em média'
        
    else:
        comp = 'Os  data centers consomem mais água em média'
    
    
    
    print(f'\n{comp} \nOs valores médios calculados são de: \n ->{mediax:.2f}L para os data centers\n ->{mediay:.2f}L para as famílias')