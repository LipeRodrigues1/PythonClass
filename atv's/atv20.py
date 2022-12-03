#posicao_alunos
import random

a1 = str(input('Digite o nome do aluno 1'))
a2 = str(input('Digite o nome do aluno 2'))
a3 = str(input('Digite o nome do aluno 3'))
a4 = str(input('Digite o nome do aluno 4'))
lis = [a1, a2, a3, a4]
random.shuffle(lis)

print(f'A ordem dos alunos é {lis}')
