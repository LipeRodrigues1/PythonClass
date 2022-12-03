#velocidade_carro

vel = float(input('Seu carro esta a quantos KM?'))
limite = 80
multa = (vel - limite) * 7
if vel > limite:
    print('Vc vai ser multado!')
    print('R$',multa)
else:
    print('Diriga com cuidado em !')



