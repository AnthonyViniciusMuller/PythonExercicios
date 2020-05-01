lado1 = float(input("Qual é o tamanho do primeiro lado: "))
lado2 = float(input("Qual é o tamanho do segundo lado: "))
lado3 = float(input("Qual é o tamanho do terceiro lado: "))

if lado1 < lado2+lado3 and lado2 < lado1+lado3 and lado3 < lado1+lado2:
    print("Pode-se formar um triângulo!")
else:
    print("Não se pode criar um trângulo!")
