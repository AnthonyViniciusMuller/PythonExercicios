money = int(input("Quanto dinheiro você quer sacar: "))
contador_50 = 0
contador_20 = 0
contador_10 = 0
contador_1 = 0
while True:
    contador_50 = money // 50
    money = money % 50
    contador_20 = money // 20
    money = money % 20
    contador_10 = money // 10
    money = money % 10
    contador_1 = money // 1
    money = money % 1
    break
print(f"Você recebeu \n{contador_50} nota(s) de 50\n{contador_20} nota(s) de 20\n{contador_10} nota(s) de 10 \n{contador_1} nota(s) de 1.")