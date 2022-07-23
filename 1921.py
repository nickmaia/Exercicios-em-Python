#n = int(input())
#A = (n*(n-3))//2
#print("{}".format(A))

n = int(input())
s = 0
for i in range(n):
  s += i
s -= n
print(s)