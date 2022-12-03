#advinhar
import random
pc = random.randint(0, 5)
jogador = int(input('Em que número eu pensei? '))

if jogador == pc:
    print('PARABENS!')
else:
    print(f'PERDEU! O Pc pensou no {pc} e eu pensei no {jogador}')







