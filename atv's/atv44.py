#pagamentos
print('========= LIPE LOJAS ===========')
gasto = float(input('Qual o total da divida? R$'))
print('''
[ 1 ] A vista Dinheiro/Cheque
[ 2 ] A vista Cartão
[ 3 ] 2x no Cartão
[ 4 ] 6x no Cartão''')

opcao = int(input('Selecione uma forma de pagamento: '))

if opcao == 1:
    desc = gasto - (gasto * 15/100)
elif opcao == 2:
    desc = gasto - (gasto * 5/100)
elif opcao == 3:
    print(f'O valor de {gasto}R$ ficará o mesmo!')
elif opcao == 4:
    desc = gasto + (gasto * 20/100)
    print(f'A sua divida de {gasto}R$ ficara assim: {desc}R$  ')









