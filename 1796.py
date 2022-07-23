# "0" os que consideram o cenário atual satisfatório e "1" os que consideram não satisfatório.


N = int(input())
lista = input().split()

A = lista.count("0")
B = lista.count("1")

if (A>B):
    print("Y")
else:
    print("N")