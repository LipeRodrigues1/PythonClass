#IMC

peso = float(input('Qual seu peso? (Kg)'))
altura = float(input('Qual sua altura (M)'))

IMC = peso / (altura ** 2)

print(f'Seu IMC é de {IMC:.2f}')
if IMC < 18.5:
    print('Abaixo do peso')
elif 18.5 <= IMC < 25:
    print('Peso Ideal')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30 <= IMC < 40:
    print('Obesidade')
else:
    print('Abesidade Morbida')

