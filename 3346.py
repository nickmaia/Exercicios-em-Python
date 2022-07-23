"""
Cada flutuação é expressa por uma porcentagem, 
de modo que uma porcentagem positiva indica crescimento naquele período de um ano, 
enquanto que uma porcentagem negativa indica decrescimento.
"""

a, b = map(float, input().split())

flutuacao = (((1.0 + a / 100.00) * (1.0 + b / 100.00)) - 1.0) * 100.0
print("{:.6f}".format(flutuacao))