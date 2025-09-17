from random import randint
itens = ['pedra', 'papel', 'tesoura']
computador = randint(0, 2)
jogador = int(input('Qual é a sua jogada? '))
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
if computador ==0: #PEDRA
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Você ganhou')
    elif jogador == 2:
        print('Você perdeu')
#------------------------------------------
elif computador == 1: #PAPEL
    if jogador == 0:
        print('Você perdeu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Você ganhou')
#------------------------------------------
elif computador == 2: #TESOURA
    if jogador == 0:
        print('Você ganhou')
    elif jogador == 1:
        print('Você perdeu')
    elif jogador == 2:
        print('Empate')
#------------------------------------------
else:
    print('Jogada inválida!')
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
