#hipotenusa
import math
cadj = float(input('Informe o cateto adjacente do triangulo: '))
cop = float(input('Informe o cateto oposto do triangulo: '))

hipo = math.hypot(cadj,cop)

print(f'A hipotenusa do triangulo vai medir {hipo:.2f}')


