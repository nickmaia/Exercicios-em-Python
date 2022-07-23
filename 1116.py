N=int(input())
while True:
    try:
        A,B = map(int,input().split())
        if(A==B):
            print("1")
        elif(B==0):
            print("divisao impossivel")
        else:
            X = A/B
            print("{}".format(X))
    except:
        break