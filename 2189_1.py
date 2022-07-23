n = int(input())
j = 1
while n != 0:
    
    ingressos = map(int, input().split())
    print("Teste {}".format(j))
    j += 1
    for i in zip(ingressos, range(1, n + 1)):
        if i[0] == i[1]:
            print(i[0])
    print()
    n = int(input())