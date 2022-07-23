
dias = int(input())
    
ANOS = int(dias/365)
MESES = int((dias-(365* ANOS))/30)
DIAS = int(dias-(ANOS*365)-(MESES*30))

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(ANOS,MESES,DIAS))



