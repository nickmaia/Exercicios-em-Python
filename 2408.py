A,B,C = map(int,input().split())

maior = max(A,B,C)
menor = min(A,B,C)
soma = A+B+C
Valor = soma - maior - menor
print("{}".format(Valor))