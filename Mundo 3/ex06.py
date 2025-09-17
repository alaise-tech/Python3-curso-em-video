#LISTAS
#Maiores e menores valores em uma lista
lista = []
for c in range(0, 5):
    n = int(input(f'Digite um valor para a posição {c}: '))
    lista.append(n)
    if c == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('-='*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
