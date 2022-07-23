#humanos, elfos e anões (lado do bem) têm que se unir para combater os orcs e os wargs (lado do mal)
H,E,A,O,W,X = map(int,input().split())
EXB=H+E+A
EXM=O+W
EXBX= H+E+A+X
if(EXB>EXM):
    print("Middle-earth is safe.")
elif(EXBX>EXM):
    print("Middle-earth is safe.")
elif((EXBX+1>EXM)):
    print("Middle-earth is safe.")
else:
    print("Sauron has returned.")
