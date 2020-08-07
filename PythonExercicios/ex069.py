contador_18 = 0
contador_homens = 0
contador_20 = 0

while True:
    print("~~~~~~~~~~~~~~~ Cadastro ~~~~~~~~~~~~~~~")
    idade = int(input("Digite a idade: "))
    while idade < 0:
        idade = int(input("Invalido! Digite a idade: "))
    sexo = str(input("Digite o sexo[F/M]: ")).strip().upper()[0]
    while sexo not in "MF":
        sexo = str(input("Invalido! Digite o sexo[F/M}: ")).strip().upper()[0]
    if sexo in "M":
        contador_homens += 1
    if sexo in "F" and idade < 20:
        contador_20 += 1
    if idade > 18:
        contador_18 += 1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    escolha = str(input("Deseja cadastrar mais alguem[S/N]: ")).strip().upper()[0]
    while escolha not in "SN":
        escolha = str(input("Invalido! Deseja cadastrar mais alguem[S/N]: ")).strip().upper()[0]
    if escolha in "N":
        break

print(f"Foram cadastrada(s) {contador_18} pessoa(s) com mais de 18 anos, {contador_homens} homen(s) e {contador_20} mulhere(s) com menos de 20 anos.")