#aluguel_de_carros
dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro rodou? '))
aluguel = (dias * 60) + (km * 0.15)
print(f'O carro foi alugado por {dias} dias e percorreu {km} km/h, seu aluguel custou {aluguel}')



