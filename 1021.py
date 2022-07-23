A = float(input())

NOTA100 = int(A//100)
A = A - (NOTA100 *100)

NOTA50 = int(A//50)
A = A - (NOTA50 *50)

NOTA20 = int(A//20)
A = A - (NOTA20 *20)

NOTA10 = int(A//10)
A = A - (NOTA10 *10)

NOTA5 = int(A//5)
A = A - (NOTA5 *5)

NOTA2 = int(A//2)
A = A - (NOTA2 *2)

NOTA1 = int(A//1)
A = A - (NOTA1 *1)

MOEDA_0_50 =int( A//0.5)
A = A - (MOEDA_0_50 *0.5)

MOEDA_0_25 =int(A//0.25)
A = A - (MOEDA_0_25 *0.25)

MOEDA_0_10 = int(A//0.10)
A = A - (MOEDA_0_10 *0.10)

MOEDA_0_05 = int(A//0.05)
A = A - (MOEDA_0_50 *0.05)

MOEDA_0_01 = abs(int(A//0.01))
A = A - (MOEDA_0_01 *0.01)


print("NOTAS:")
print("{} nota(s) de R$ 100,00".format(NOTA100))
print("{} nota(s) de R$ 50,00".format(NOTA50))
print("{} nota(s) de R$ 20,00".format(NOTA20))
print("{} nota(s) de R$ 10,00".format(NOTA10))
print("{} nota(s) de R$ 5,00".format(NOTA5))
print("{} nota(s) de R$ 2,00".format(NOTA2))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(NOTA1))
print("{} moeda(s) de R$ 0.50".format(MOEDA_0_50))
print("{} moeda(s) de R$ 0.25".format(MOEDA_0_25))
print("{} moeda(s) de R$ 0.10".format(MOEDA_0_10))
print("{} moeda(s) de R$ 0.05".format(MOEDA_0_05))
print("{} moeda(s) de R$ 0.01".format(MOEDA_0_01))