#menor_maior

n1 = float(input('Digite o primeiro valor '))
n2 = float(input('Digite o segundo valor '))
n3 = float(input('Digite o terceiro valor '))

menor = n1

if n2 < n1 and n3 < n1:
    menor  = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Verificando o menor

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O maior número foi {maior}')
print(f'O menor número foi {menor}')
