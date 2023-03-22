import time

def pot_conj(n):
    pot = []
    for subconj in range(2**(n*n)):
        pot.append(conjPares(subconj,n))
    return pot
    
def conjPares(s,n):
    conj = []
    for i in range(n):
        for j in range(n):
            if bitLigado(i,j,n,s):
                conj.append((i+1,j+1)) 
    return conj

def bitLigado(i,j,n,s):
    return s&(1<<(i*n+j))!=0

n = 4


start_time = time.time()

resultado = pot_conj(n)


end_time = time.time()


total_time = end_time - start_time


with open("resultado_relações.txt", "w") as output_file:
    for relacao in resultado:
        s = set(relacao)
        tamanho = len(s)
        simetrica = s == s.symmetric_difference(set([(y, x) for (x, y) in s]))
        reflexiva = all((x, x) in s for x in range(1, n+1))
        transitiva = all((a, c) in s for (a, b) in s for (c, d) in s if b == c)
        irreflexiva = all((x, x) not in s for x in range(1, n+1))
        equivalencia = simetrica and reflexiva and transitiva
        bijetora = tamanho == n and equivalencia
        sobrejetora = tamanho == 2**n-1
        injetora = tamanho == n

        classificacao = ""
        if simetrica:
            classificacao += "S"
        if transitiva:
            classificacao += "T"
        if reflexiva:
            classificacao += "R"
        if equivalencia:
            classificacao += "E"
        if irreflexiva:
            classificacao += "I"
        if injetora:
            classificacao += "Fi"
        if sobrejetora:
            classificacao += "Fs"
        if bijetora:
            classificacao += "Fb"

        output_file.write(str(s) + " " + classificacao + "\n")

print("Tempo total de execução:", total_time, "segundos")
