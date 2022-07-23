N,A,B = map(int,input().split())

while(N !=0  and A!=0 and B!=0):
    lista1=[]

    i=0
    j=0
    for i in range(1,N+1,A):
        lista1.append(i)
    for j in range(1,N+1,B):
        if j not in lista1:
            lista1.append(j)

    print(len(lista1))
    N,A,B = map(int,input().split())