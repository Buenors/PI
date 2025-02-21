#Verifique se o primeiro número é múltiplo do segundo. 

n1 = float(input("Número: "))
n2 = float(input("Número múltiplo: "))

if n2 == 0:
    
    print("Número múltiplo não pode ser 0")
    
else:
    
    m = n1%n2
    
    if m != 0:
        
        print(f"O primeiro ({n1}) não é múltiplo do segundo({n2})")
        
    else:
        
        print(f"O primeiro ({n1}) é múltiplo do segundo({n2})")