A = int(input())

if (A == 0):
    resp = "E"
if (A >= 1 and A <= 35):
    resp = "D"
if (A >= 36 and A <= 60):
    resp = "C"
if (A >= 61 and A <= 85):
    resp = "B"
if (A >= 86 and A <= 100):
    resp = "A"

print(resp)