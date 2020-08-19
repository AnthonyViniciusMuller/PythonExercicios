times = ('Corintians', 'Palmeiras', 'Santos', 'Grêmio','Cruzeiro', 'Flamengo', 'Vaco', 'Chapecoense',
         'Atletico', 'BotaFogo', 'Atletico-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'Ec Vitoria', 'Curitiba', 'Avaí', 'Ponte Preta', 'Atletico-GO')

print("=" * 50)
print("Primeiros 5 colocados")
print(times[0:5])

print("=" * 50)
print("Ultimos 4 colocados")
print(times[-4:])

print("=" * 50)
print("Times em ordem alfabetica")
print(sorted(times))

print("=" * 50)
print("Posição do chapecoense")
print(times.index("Chapecoense"))
