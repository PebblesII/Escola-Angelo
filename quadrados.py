quadrado = [x**2 for x in range(1, 6)]

print(quadrado)

quadrados2 = []
for x in range(1, 6):
    quadrados2.append(x**2)


print(quadrados2)


pares = [x for x in range(10) if x %2 == 0]
print(pares)


pares2 = []
for x in range(10):
    if x % 2 == 0:
        pares2.append(x)
print(pares2)


mesagem = ["Hoje", "estou", "animado!"]
maisculo = [msg.upper() for msg in mesagem]

print(mesagem)
print(maisculo)


mesagem2 = ["a"]
maisculo2 = []

for msg in mesagem2:
    maisculo2.append(msg.upper())

print(mesagem2)
print(maisculo2)

