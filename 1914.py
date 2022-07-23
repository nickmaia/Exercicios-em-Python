QT = int(input())
while True:
    try:

        J1,X,J2,Y = map(str,input().split())
        N1,N2 = map(int,input().split())

        M = N1+N2

        if(M % 2==0):
           P = "PAR"
        else:
            "IMPAR"
        
        if P == X:
            print(J1)
        else:
            print(J2)
    except:
        break  