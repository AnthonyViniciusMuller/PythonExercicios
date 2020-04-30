import random

aluno1 = str(input("Qual é o nome do primeiro aluno: "))
aluno2 = str(input("Qual é o nome do segundo aluno: "))
aluno3 = str(input("Qual é o nome do terceiro aluno: "))
alunos = [aluno1, aluno2, aluno3]

aluno = random.choice(alunos)

print("O aluno escolhido foi {}".format(aluno))
