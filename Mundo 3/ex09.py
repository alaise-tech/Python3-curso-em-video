#LISTAS
# Extraindo dados de uma lista
valores = []  # Lista onde serão armazenados os valores
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

# Imprimindo os valores da lista com suas posições
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

# Informações sobre a lista
print('Cheguei ao final da lista.')
print(f'Essa lista tem {len(valores)} elementos.')  # Mostrando a quantidade de elementos da lista
print(valores)  # Mostrando a lista completa
    