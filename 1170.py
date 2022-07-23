Numero_de_testes = int(input())


while Numero_de_testes > 0:
    Numero_de_testes = Numero_de_testes - 1
    Dias = 0
    Comida = float(input())
    
    while Comida > 1:
        Dias = Dias + 1
        Comida = Comida/2

    
    print('{} dias'.format(Dias))
