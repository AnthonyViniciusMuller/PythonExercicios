mulherMenor = 0
maiorIdade = 0
maisVelho = ''
mediaIdade = 0
for c in range(5):
    print("===================== {} pessoa =====================".format(c + 1))
    nome = str(input("Nome: ")).strip().capitalize()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).lower().strip()
    mediaIdade += idade
    if c == 0 and sexo == "m":
        maiorIdade = idade
        maisVelho = "nome"
    elif maiorIdade < idade and sexo =="m":
        maiorIdade = idade
        maisVelho = nome

    if sexo == "f" and idade < 20:
        mulherMenor += 1

mediaIdade /= c

print("A média da idade do grupo é {:.2f} anos".format(mediaIdade))
print("O homem mais tem {} anos e se chama {}".format(maiorIdade, maisVelho))
print("Ao todo são {} mulheres menores de 20 anos".format(mulherMenor))
