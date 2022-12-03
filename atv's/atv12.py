#Preco_com_desconto
prod = float(input('Qual o preço do produto? '))
desc = prod * 5/100
novopord = prod - desc

print(f'O produto que custa {prod}R$ com o desconto de 5% vai custar {novopord}')
