
valor = int(input())
letra = input()
soma = 0.0
matriz = [] 
for i in range(12):
    linha = [] 
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha) 
for j in matriz:
    soma+=j[valor]

media = soma/12.0

if(letra=="S"):
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(media))