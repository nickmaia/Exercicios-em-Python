a,b,c = map(float,input().split())


Area_triagulo = (a*c)/2
Area_circulo =  3.14159* (c**2)
Area_trapezio = ((a+b)*c)/2
Area_quadrado = b**2
Area_retangulo = a * b

print("TRIANGULO: {:.3f}".format(Area_triagulo))
print("CIRCULO: {:.3f}".format(Area_circulo))
print("TRAPEZIO: {:.3f}".format(Area_trapezio))
print("QUADRADO: {:.3f}".format(Area_quadrado))
print("RETANGULO: {:.3f}".format(Area_retangulo))
