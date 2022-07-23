"""
 G galhos, ela precisa G/2 bolinhas. Se o número G de galhos for ímpar, esse valor será arredondado para baixo.
  quantidade de bolinhas que Amélia já possui e a quantidade de galhos de sua nova árvore de natal.
  Se o número G de galhos for ímpar, esse valor será arredondado para baixo.

  Imprima a quantidade de bolinhas que Amélia precisa comprar para completar sua árvore, com a mensagem "Faltam B bolinha(s)", 
  onde B é a quantidade de bolinhas que Amelia precisa comprar. 
  Caso Amelia possua bolinhas suficientes ou de sobra, imprima a mensagem "Amelia tem todas bolinhas!"
"""

bolinhas_possui = int(input())
galhos = int(input())

if (galhos % 2 != 0):
    bolinhas_precisa = (galhos - 1) / 2
else:
    bolinhas_precisa = galhos / 2

if (bolinhas_possui >= bolinhas_precisa):
    print("Amelia tem todas bolinhas!")
else:
    bolinhas = bolinhas_precisa - bolinhas_possui
    print("Faltam {:.0f} bolinha(s)".format(bolinhas))