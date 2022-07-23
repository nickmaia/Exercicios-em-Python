#A entrada contém vários casos de teste.
#quatro números inteiros H  1 , M 1 , H2 e M 2
#H1:M1 representando a hora e minuto atuais
#H2:M2 representando a hora e minuto para os quais o alarme  despertador foi programado
#0≤H1≤23, 0≤M1≤59, 0≤H2≤23, 0≤M2 ≤59

H1, M1, H2, M2 = map(int,input().split())

Minutos_iniciais = H1*60 + M1
Minutos_finais = H2*60 + M2
I = H1 + H2 + M1 + M2


while I != 0:
    if H1 < H2 and M1 < M2:
        Tempo_minutos_totais = Minutos_finais - Minutos_iniciais
        print (Tempo_minutos_totais)
    elif H1 < H2 and M1 > M2:
        Tempo_minutos_totais = Minutos_finais - Minutos_iniciais
        print (Tempo_minutos_totais)
    elif  H1 < H2 and M1 == M2:
        Tempo_minutos_totais = Minutos_finais - Minutos_iniciais
        print (Tempo_minutos_totais)



    elif H1 == H2 and M1 < M2:
        Tempo_minutos_totais = Minutos_finais - Minutos_iniciais
        print (Tempo_minutos_totais)
    elif H1 == H2 and M1 > M2:
        Tempo_minutos_totais = 24*60 - (M1 - M2)
        print(Tempo_minutos_totais)
    elif H1 == H2 and M1 == M2:
        Tempo_minutos_totais = 24*60
        print(Tempo_minutos_totais)



    elif H1 > H2 and M1 < M2:
        Tempo_minutos_totais = (24 - (H1 - H2))*60 + (M2 - M1)
        print(Tempo_minutos_totais)
    elif H1 > H2 and M1 > M2:
        Tempo_minutos_totais= (24 - (H1 - H2))*60 - (M1 - M2)
        print(Tempo_minutos_totais)
    elif H1 > H2 and M1 == M2:
        Tempo_minutos_totais = (24 - (H1 -H2))*60
        print(Tempo_minutos_totais)


    H1, M1, H2, M2 = map(int,input().split())
    Minutos_iniciais = H1*60 + M1
    Minutos_finais = H2*60 + M2
    I = H1 + H2 + M1 + M2
    