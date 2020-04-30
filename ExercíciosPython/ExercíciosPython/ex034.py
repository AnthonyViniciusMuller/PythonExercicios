salario = float(input("Qual é o seu salário: "))

if salario > 1250:
    s_atual = salario + (salario*0.1)
else:
    s_atual = salario + (salario*0.15)

print("O salário de {} reais passa a ser {} reais".format(salario, s_atual))