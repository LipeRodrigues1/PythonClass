#triângulos

s1 = float(input('Primeira reta: '))
s2 = float(input('Segunda reta: '))
s3 = float(input('Terceira reta: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('As restas podem formar um triângulo!')
    if s1 == s2 == s3:
        print('Triângulo EQUILATERO!')
    elif s1 != s2 != s3 != s1:
        print('Triângulo ESCALENO!')
    else:
        print('Triângulo ISÓSCELES!')
else:
    print('Não forma triângulo!')


