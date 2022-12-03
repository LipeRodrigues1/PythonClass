#viagem

dist = float(input('Qual a distancia em KM da viagem? '))
curta = dist * 0.50
longa = dist * 0.45

if dist <= 200:
    print(f'Sua viagem vai custar R${curta}')
elif dist > 200:
    print(f'Sua viagem vai custar R${longa}')




