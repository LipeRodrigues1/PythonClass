#classificação

from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano

if idade <= 9:
    print(f'Por ter {idade} anos voce é MIRIM')
elif idade <= 14:
    print(f'Por ter {idade} anos voce é INFANTIL')
elif idade <= 19:
    print(f'Por ter {idade} anos voce é JUNIOR')
elif idade <=25:
    print(f'Por ter {idade} anos voce é SENIOR')
elif idade > 25:
    print(f'Por ter {idade} anos voce é MASTER')


