#JO KEN PO
from random import randint
from time import sleep
itens = ('Pedra', 'Papel ', 'Tesoura ')
pc = randint(0,2)

print(f'O Computador escolheu {itens[pc]}')
print('''Escolha entre:
[ 0 ] Pedra 
[ 1 ] Papel
[ 2 ] Tesoura''')
eu = int(input('Qual é a jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('='*20)
print(f'O Pc jogou {itens[pc]}')
print(f'Eu joguei {itens[eu]}')
print('='*20)

if pc == 0:
    if eu == 0:
        print('EMPATE!')
    elif eu == 1:
        print('EU VENCI!')
    elif eu == 2:
        print('EU PERDI!')
    else:
        print('INVALIDO!')

elif pc == 1:
    if eu == 0:
        print('EU PERDI!')
    elif eu == 1:
        print('EMPATE!')
    elif eu == 2:
        print('EU VENCI!')
    else:
        print('INVALIDO!')

elif pc == 2:
    if eu == 0:
        print('EU VENCI!')
    elif eu == 1:
        print('EU PERDI!')
    elif eu == 2:
        print('EMPATE!')
    else:
        print('INVALIDO!')







