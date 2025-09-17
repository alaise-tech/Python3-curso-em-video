#TUPLAS
#Maior e menor valor 
from random import randint
from time import sleep
valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in valores:
    print(f'{n} ', end='', flush=True)
    sleep(0.5)
print(f'\nO maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')
