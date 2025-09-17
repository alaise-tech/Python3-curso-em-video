#Reajuste Salarial
salário = float(input("Qual é o salário do funcionário? R$"))
aumento = salário * 0.15
novo_salário = salário + aumento
print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salário, novo_salário))