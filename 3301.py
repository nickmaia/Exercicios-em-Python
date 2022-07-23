A, B, C = map(int, input().split())

meio = A + B + C - max(A, B, C) - min(A, B, C)
#H, Z e L
if (meio == A):
    print("huguinho")
elif (meio == B):
    print("zezinho")
else:
    print("luisinho")