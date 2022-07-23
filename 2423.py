A,B,C = map(int,input().split())
A<=1 and C<=100

# 2 xícaras de farinha de trigo, 3 ovos e 5 colheres de sopa de leite. 
# Em casa ele tem A xícaras de farinha de trigo, B ovos e C colheres de sopa de leite.
# 4 6 10

farinha = A//2
ovos = B//3
leite = C//5 

bolo = min(farinha,ovos,leite)
print("{}".format(bolo))
