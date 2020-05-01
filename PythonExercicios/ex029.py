velocidade = int(input("Qual é a velocidade do seu carro: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Voce foi multado em {} reais".format(multa))

print("diriga com segurança")