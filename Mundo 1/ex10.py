#Aluguel de Carros
dias = int(input("Por quantos dias você alugou o carro? "))
km = float(input("Quantos Km você rodou com o carro? "))    
preço = (dias * 60) + (km * 0.15)
print("O total a pagar é de R${:.2f}".format(preço))