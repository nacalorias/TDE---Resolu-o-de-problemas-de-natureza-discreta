#Ana Carolina Afonso Meiado 

def receber_arquivo(arquivo):
    with open(arquivo) as arquivo:
        leitura = arquivo.readlines()

def operacoes(operacao,conj1,conj2):
    conj1 = conj1.split()
    conj2 = conj2.split()
    if operacoes == 'U':
        resultado = conj1.union(conj2)
    elif operacoes == "C":
        resultado = {(x,y) for x in conj1 for y in conj2}
    elif operacoes == 'I':
        resultado = conj1.intersection(conj2)
    elif operacoes == 'D':
        resultado = conj1.difference(conj2)
    return conj1, conj2, resultado
