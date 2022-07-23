from collections import Counter
from string import ascii_lowercase
casos = int(input())
j=0
while casos > j:
    texto = input().lower()
    texto = "".join([letra for letra in texto if letra in ascii_lowercase])
    x = Counter(texto)
    freq_max = x.most_common(1)[0][1]
    letras = ""
    for i in x:
        if x[i] == freq_max:
            letras += i
    print("".join(sorted(letras)))
    j+=1

