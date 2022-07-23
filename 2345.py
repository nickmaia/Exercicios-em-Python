a,b,c,d=map(int,input().split())

maximo=max(a,b,c,d)
minimo=min(a,b,c,d)

time1=maximo+minimo
time2=a+b+c+d-time1
total=abs(time1-time2)

print(total)
