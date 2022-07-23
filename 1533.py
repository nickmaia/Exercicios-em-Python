n=int(input())

while (n!=0):
    suspeitos = list(map(int,input().split()))

    alvo=list(sorted(suspeitos,reverse=True))
    alvo1=alvo[1]

    alvo2=suspeitos.index(alvo1)

    print(alvo2+1) 

    n=int(input())