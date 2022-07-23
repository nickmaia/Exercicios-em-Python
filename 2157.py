k =int(input())
j=0
while j<k :
    A,B = map(int,input().split())
    i = ""

    while A <= B:
       i += str(A)
       A += 1

    Final = ""

    Final = i + i[::-1]

    print(Final)
    
    j = j + 1