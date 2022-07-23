N = int(input())


for i in range(0,N,1):

    texto = input().split()
    i = len(texto)
    Codigo = ''

    for i in range(0,i,1):
        

        Codigo = Codigo + '{:.1}'.format(texto[i])
    
    print(Codigo)
    
