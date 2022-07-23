# 1 Coloque sete espaços em branco e coloque o carácter 'A';
# 2 seis espaços em branco e coloque o carácter 'B', um espaço em branco e o carácter 'B';
# 3 cinco espaços em branco e coloque o carácter 'C', três espaço em branco e o carácter 'C';
# 4 quatro espaços em branco e coloque o carácter 'D', cinco espaço em branco e o carácter 'D';
# 5 três espaços em branco e coloque o carácter 'E', sete espaço em branco e o carácter 'E';
# Repita o procedimento 4;
# Repita o procedimento 3;
# Repita o procedimento 2;
# Repita o procedimento 1.

txt = "A"
x = txt.rjust(8," ") 
print(x) 
txt = "B"
x = txt.rjust(7," ") 
print(x,"B") 
txt = "C"
x = txt.rjust(6," ") 
print(x,"  C")
txt = "D"
x = txt.rjust(5," ") 
print(x,"    D")
txt = "E"
x = txt.rjust(4," ") 
print(x,"      E") 
txt = "D"
x = txt.rjust(5," ") 
print(x,"    D")
txt = "C"
x = txt.rjust(6," ") 
print(x,"  C")
txt = "B"
x = txt.rjust(7," ") 
print(x,"B")
txt = "A"
x = txt.rjust(8," ") 
print(x) 