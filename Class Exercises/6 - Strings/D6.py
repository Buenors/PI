word = input('Insira a palavra: ')
l = len(word) - 1 #Menos 1 pq começa a contagem a partir do 0
while l >= 0:
    print(word[l])
    l -= 1