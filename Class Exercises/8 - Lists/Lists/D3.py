def soma_vetorial(va , vb):   

    if len(va) == len(vb):
        vc = list()
        for i in range(len(va)):
            vc.append(va[i] + vb[i])
        return vc
    else:
        return 'Os vetores não tem o mesmo tamanho'

vetor1 = [1,2,3]
vetor2 = [2,3,4]
print(soma_vetorial(vetor1, vetor2))