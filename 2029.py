while True:
    try:

        V = float(input())
        D = float(input())

        altura = V/(3.14 * ((D/2)**2))
        area= 3.14 * ((D/2)**2)

        print("ALTURA = {:.2f}\nAREA = {:.2f}".format(altura,area))

    except:
        break