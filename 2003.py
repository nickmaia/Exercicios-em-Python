from sys import stdin

while True:
    try:
        hora,minuto = map(int,stdin.readline().split(":"))

        horatotal=hora+(minuto/60)+1
        minutosatrasado = (horatotal-8)*60

        if (horatotal<=8):{
            print("Atraso maximo: 0")
        }
        else:{
            print("Atraso maximo: {:.0f}".format(minutosatrasado))
        }
    except:
        break