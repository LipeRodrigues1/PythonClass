#sorteio
import random
n1 = str(input('Digite o primeiro item'))
n2 = str(input('Digite o segundo item'))
n3 = str(input('Digite o terceiro item'))
n4 = str(input('Digite o quarto item'))

lista = [n1,n2,n3,n4]
sorteado = random.choice(lista)
print(f'O item sorteado foi : {sorteado}')