"""
Tabuleiro 3x3: 5 casas brancas e 4 casas pretas
Tabuleiro 4x4: 8 casas brancas e 8 casas pretas
"""
numero = int(input())

n = numero * numero

if (n % 2 == 0):
    n = n / 2
    print("{:.0f} casas brancas e {:.0f} casas pretas".format(n, n))
else:
    n = int(n / 2)
    print("{:.0f} casas brancas e {:.0f} casas pretas".format(n + 1, n))
