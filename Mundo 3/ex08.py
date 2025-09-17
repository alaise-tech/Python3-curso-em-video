#LISTAS
#Lista ordenada sem repetições
num = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > num[-1]: #Se for o primeiro valor ou se for maior que o último
        num.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

