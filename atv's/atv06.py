#dobro_tripo_raiz
from math import sqrt
n = int(input('Digite um valor '))

dobro = n * 2
triplo = n * 3
raiz = sqrt(n)#pow(n,(1,2))

print(f'O dobro de {n} é {dobro}')
print(f'O triplo de {n} é {triplo}')
print(f'A raiz de {n} é {raiz:.2f}')#:.2f = 2 casas decimais