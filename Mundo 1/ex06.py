#Conversor de Moedas
real = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = real / 5.20
print("Com R${:.2f} você pode comprar U${:.2f}".format(real, dolar))
