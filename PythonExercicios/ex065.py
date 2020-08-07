n1 = int(input("Digite um número: "))
resposta = str(input("Deseja continuar[S/N]: ")).strip().upper()
media = n1
maior = n1
menor = n1
contador = 1

while resposta not in 'N':
    contador += 1
    n1 = int(input("Digite um número: "))
    resposta = str(input("Deseja continuar[S/N]: ")).strip().upper()
    media += n1
    if maior < n1:
        maior = n1
    if menor > n1:
        menor = n1

media /= contador
print("Foram digitados {} números, com uma média de {}.\nO maior foi {} e o menor foi {}".format(contador, media, maior, menor))