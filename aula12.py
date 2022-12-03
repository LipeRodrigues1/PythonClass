#condicoes_aninhadas

idade = int(input('Qual a sua idade? '))

if idade == 17:
    print('Você é menor de idade!!')
elif idade >= 18 and idade <= 50:
    print('Já esta maior de idade!')
elif idade >=51 and idade <=70:
    print('Já ta idoso ein')
else:
    print('Betinha????')

print(f'Essa é sua faixa etaria já que tem {idade} anos')


