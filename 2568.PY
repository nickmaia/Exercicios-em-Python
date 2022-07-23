"""dias pares, 
o preço da ação sobe X reais em relação ao preço do final do dia anterior.
Nos dias ímpares, 
o preço da ação já se inicia com um valor X reais abaixo do valor no fim do dia anterior.
1 10 5 3      15
1 10 5 2      10
2 10 5 3      5
"""
Dia_inicial,preco_inicial,Variacao_diaria,Dia_final = map(int,input().split())


resultado_final = preco_inicial
i=0
for i in range(Dia_inicial,Dia_final,1):

    if (i%2==0):
        resultado_final-=Variacao_diaria
        
    else:
        resultado_final+=Variacao_diaria
        
print(resultado_final)
