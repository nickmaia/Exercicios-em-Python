letra = input()
texto = str(input().split())
tam = len(texto)
txt = texto.count(letra)
final = (txt/tam)*100

print("{:.1f}".format(final))
