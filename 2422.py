
N = int(input())
casas = dict()


for i in range(N):
    casa = int(input())
    casas[casa] = 1

k = int(input())

for i in casas:
    valor = k - i
    if valor in casas:
        print(i, valor)
        break


