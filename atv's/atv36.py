#emprestimo

valcasa = float(input('Qual o valor desta casa? R$'))
salario = float(input('Quaal é o seu salario? R$'))
parcelas = int(input('Em quantos anos sera parcelada? '))

emprest = valcasa / (parcelas * 12)
mini = salario * 30/100

print(f'Para comprar essa casa no valor de {valcasa}R$ em {parcelas} anos a prestação será de {emprest:.2f}R$')
if emprest<= mini:
    print('Emprestimo CONCEDIDO!!')
else:
    print('Emprestimo negado!')


