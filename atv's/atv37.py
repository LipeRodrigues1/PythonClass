#Conversor_de_bases
n = int(input('Digite um número '))
print('''Escolha uma base para converter:  
[ 1 ]BINÁRIO
[ 2 ]OCTAL
[ 3 ]HEXA     ''')
opcao = int(input('Escolha uma opção: '))
if opcao == 1:
    print(f'{n} convertido em binário é igual a {bin(n)} ')
elif opcao == 2:
    print(f'{n} convertido em OCTAL é igual a {oct(n)} ')
elif opcao == 3:
    print(f'{n} convertido a HEXA é igual a {hex(n)}')
else:
    print('Opção Invalida!!')


