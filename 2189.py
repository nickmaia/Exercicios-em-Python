n = int(input())
i=1
while(n!=0):
    print("Teste {}".format(i))
    i+=1
    
    print(list(filter(
        lambda x: x[0]==x[1],
        zip(map(int, input().split()), range(1, n + 1)),
    ))[0][0])
    print()
    n = int(input())