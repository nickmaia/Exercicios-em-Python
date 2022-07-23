Numero_soldados = int(input())
Quadragonia = map(int,input().split(" "))
Noglonia = map(int,input().split(" "))

Quadragonia = list(Quadragonia)
Noglonia = list(Noglonia)
y=0
for x in zip(Noglonia,Quadragonia):
    if x[0] > x[1]:
        y=y+1
print(y)