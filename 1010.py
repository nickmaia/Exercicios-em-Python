A1,B1,C1 = map(float,input().split())
A2,B2,C2 = map(float,input().split())

recibo = (B1*C1)+(B2*C2)

print("VALOR A PAGAR: R$ {:.2f}".format(recibo))