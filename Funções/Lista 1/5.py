#Tirar carteira

i = int(input('Insira sua Idade: '))

ct = input('Concluiu  o curso teórico (responda com T/F): ')
cp = input('Concluiu  o curso prático (responda com T/F): ')

if i >= 18 and ct == "T" and cp == "T":
    print("Pode tirar a carteira")

elif i>=18 and ct =="T" or cp == "T":
    print("Pode tirar a carteira mas antes deve concluir o outro curso")
    
else: print("não pode tirar a carteira")

