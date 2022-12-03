#pintando_parede
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg * alt
print(f'Sua parede tem as dimensões {larg}X{alt} e mede {area}m²')

tinta = area/2
print(f'Para pintar essa parede toda será necessario {tinta}L ao todo')




