A = int(input())
x = A

NOTA100 = A//100
A = A - (NOTA100 *100)

NOTA50 = A//50
A = A - (NOTA50 *50)

NOTA20 = A//20
A = A - (NOTA20 *20)

NOTA10 = A//10
A = A - (NOTA10 *10)

NOTA5 = A//5
A = A - (NOTA5 *5)

NOTA2 = A//2
A = A - (NOTA2 *2)

NOTA1 = A//1
A = A - (NOTA1 *1)

print("{}".format(x))
print("{} nota(s) de R$ 100,00".format(NOTA100))
print("{} nota(s) de R$ 50,00".format(NOTA50))
print("{} nota(s) de R$ 20,00".format(NOTA20))
print("{} nota(s) de R$ 10,00".format(NOTA10))
print("{} nota(s) de R$ 5,00".format(NOTA5))
print("{} nota(s) de R$ 2,00".format(NOTA2))
print("{} nota(s) de R$ 1,00".format(NOTA1))