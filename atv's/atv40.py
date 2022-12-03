#media

n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))

media = (n1 + n2) / 2

if media < 7:
    print(f'Tirando {n1} e {n2} teve media {media} REPROVADO!!')
elif media >= 7:
    print(f'Tirando {n1} e {n2} teve media {media} APROVADO!!')