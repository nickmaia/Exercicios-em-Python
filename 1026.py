while True:
    try:

        a, b = map(int,input().split())
        a = int(bin(a)[2::])
        b = int(bin(b)[2::])

        soma = str(a+b)

        print(int(soma.replace("2","0"),2))
    except:
        break