numero = int(input())

while numero != 0:
    trabalhos = list(map(int, input().split()))
    resultado = max(trabalhos) * 2 - sum(trabalhos)
    print(f"{abs(resultado)}\n")
