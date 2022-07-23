Segundos = int(input())

HORAS = int(Segundos/3600)
MINUTOS = int((Segundos-(3600*HORAS))/60)
SEGUNDOS = int(Segundos-(HORAS*3600)-(MINUTOS*60))

print("{}:{}:{}".format(HORAS,MINUTOS,SEGUNDOS))




