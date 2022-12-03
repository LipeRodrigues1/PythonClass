#alistamento
from datetime import date

print('''===============================
     ALISTAMENTO MILITAR
===============================   
''')
atual = date.today().year
ano = int(input('Em que ano voce nasceu? '))
idade = atual - ano
sexo = str(input('Digite seu sexo: '))

print(f'Nascidos no ano {ano} tem {idade} anos em {atual}')


if sexo == 'Masculino':
    print('Precisa se alistar!')
elif idade == 18:
    print('Já esta na hora de se alistar!!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Faltam {saldo} anos para se alistar!')
elif idade > 18:
    saldo = idade - 18
    print(f'Já se alistou há {saldo} anos!!')
#else:
    print('Não precisa se alistar!')
