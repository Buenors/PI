def identidade(n):
    matriz = [[0 for x in range(n)] for x in range(n)]
    for l in range(n):
        for c in range(n):
            if l == c:            
                matriz[l][c] = 1
            else:
                matriz[l][c] = 0  
    for linha in matriz:
        print(linha)            


identidade(4)