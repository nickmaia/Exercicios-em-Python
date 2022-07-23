A = list(input().split())
B = list(input().split())
C = list(input().split())
D = list(input().split())
E = list(input().split())
F = int(input())


for i in A:
    lista = max(A)
    for j in B:
        lista = max(B)
        for k in C:
            lista = max(C)
            for l in D:
                lista = max(D)
                for m in E:
                    lista = max(E)
                    lista=sorted(list(i+j+k+l+m))
 


print(lista)