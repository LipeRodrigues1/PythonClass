#aumento de salario

salario = float(input('Qual é o seu salario? '))

if salario <= 1250:
    aumento = salario + (salario * 15/100)
else:
    aumento = salario + (salario * 10/100)

print(f'Quem ganhava R${salario} vai passa a ganhar R${aumento}.')
