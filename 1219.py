from math import sqrt,pi
while True:
    try:
        a,b,c = map(float,input().split())
        p = (a + b + c) / 2
        triangulo = sqrt(p*(p-a)*(p-b)*(p-c))

        d = sqrt((a+b+c)*(b+c-a)*(c+a-b)*(a+b-c))

        raioex= (a*b*c)/d
        circulomaior=pi*(raioex**2)
        circulomenor = pi*((triangulo/p)**2)
        areacirculomaior= circulomaior - triangulo 
        areatriangulo = triangulo - circulomenor
        areacirculomenor = circulomenor

        print("{:.4f} {:.4f} {:.4f}".format(areacirculomaior,areatriangulo,areacirculomenor))
    except:
        break