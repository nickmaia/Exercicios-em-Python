A,B,C = map(int,input().split())
maiorab = (A+B+abs(A-B))//2
maior = (maiorab+C+abs(maiorab-C))//2
print("{} eh o maior".format(maior))
