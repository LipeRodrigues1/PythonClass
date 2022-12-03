#manipulando_strings
texto = ('    Esse é um Texto de Exemplo')

#======Comprimento=====
print(len(texto))
print(texto.count('e'))
print(texto.find('um'))
print(texto[8])

#=====Fatiando=======
print(texto[10:15])
print(texto[10:15:2])
print(texto[5::3])

#============================TRANSFORMATION_STR==================================
print(texto.replace('Texto', 'Nuggets'))
print(texto.capitalize())
print(texto.upper())
print(texto.strip())
print()

#==================DIVISOR==========================
print(texto.split())
print('-'.join(texto))
div = texto.split()
print(div[0][3])

