#pares
soma = 0
for i in range(0,6):
    num = float(input('Digite um número '))
    if num % 2 ==0:
        soma += num
print(f'A soma entre os pares é {soma}')

