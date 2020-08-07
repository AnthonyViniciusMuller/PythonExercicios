sexo = str(input("Qual é o seu sexo[M/F]: ")).upper().strip()

while sexo not in "M" and sexo not in "F":
    sexo = str(input("Qual é o seu sexo[M/F]: ")).upper().strip()

print("Sexo confimardo,", sexo)