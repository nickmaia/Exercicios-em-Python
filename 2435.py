#o número da charrete, a sua distância à linha de chegada em metros, e a sua velocidade
N1,D1,V1= map(int,input().split())
N2,D2,V2= map(int,input().split())

K1 = (D1/1000)/V1
K2 = (D2/1000)/V2

if(K1<K2):
    print("{}".format(N1))
else:
    print("{}".format(N2))