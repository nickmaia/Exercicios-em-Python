from math import sqrt
while True:
    try:
        D,VL,VG  = map(int,input().split())

        hip=sqrt((12)**2+(D)**2)
        tempobandido = 12/VL
        distpolicia = tempobandido*VG
        
        if (distpolicia>=hip):print("S") 
        else: print("N")

    except:
        break