#Comparando numeros 
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print('O PRIMEIRO valor e maior')
elif n2 > n1:
    print('O SEGUNDO valor e maior')
else:
    print('Nao existe valor maior, os dois sao iguais')