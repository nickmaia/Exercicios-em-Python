while True:
    try:

        Juan, Ricardinho = map(int, input().split())
        notas_Juan = list(map(int, input().split()))
        notas_Ricardinho = list(map(int, input().split()))

        for i in zip(notas_Juan, notas_Ricardinho):
            if i[0] == [1]:
                print("sim")
            else:
                print("não")

    except:
        break