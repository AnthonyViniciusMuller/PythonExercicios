conta = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze','dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n1 = int(input("Escolha um número, entre 0 e 20, para ser escrito por extenso: "))
    if 0 <= n1 <= 20:
        print(conta[n1])
        break