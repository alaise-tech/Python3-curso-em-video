#LISTAS
#Valores Únicos
num = [2, 5, 9, 1]
num[2] = 3 #Alterando o valor do índice 2
num.append(7) #Adicionando o valor 7 no final da lista
num.sort() #Colocando em ordem crescente
num.sort(reverse=True) #Colocando em ordem decrescente
num.insert(2, 0) #Adicionando o valor 0 no índice
num.pop() #Removendo o último valor da lista
num.pop(2) #Removendo o valor do índice 2
num.remove(5) #Removendo o valor 5 da lista
if 4 in num:
    num.remove(4) #Removendo o valor 4 da lista, se existir
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.') #Mostrando a quantidade de
