name = input("Digíte o nome do jogo: ")
yearLaunch = int(input("Ano de lançamento: ")) 
gamePrice = float(input("Preço do jogo: "))
planIncluded = bool(input("Está incluso no serviço mensal? "))

# primeira forma de concatenar 
#print("### Dados do jogo ###")
#print("=====================")
#print("Nome do jogo:", name)
#print("Ano de lançamento:", yearLaunch)
#print("Valor do jogo:", gamePrice)
#print("Está incluso no serviço mensal:", planIncluded)
#print("=====================") 

# segunda forma de concatenar 

#print("Nome do jogo:",name,"\n Ano de lançamento:",yearLaunch,"\n Valor do jogo:",gamePrice,"\n Está incluso no plano?", planIncluded)

# terceira forma de concatenar (fstring)
print(f"Nome do jogo: {name} \nano de lançamento: {yearLaunch} \nPreço do jogo: {gamePrice} \nEstá incluso no plano? {planIncluded}")