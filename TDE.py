#Ana Carolina Afonso Meiado 


#Esse programa recebe como entrada um arquivo de texto
# contendo vários conjuntos de dados e operações. 
# A primeira linha contém o número de operações, sendo elas:
# U: união, I: interseção, D: diferença, C: produto cartesiano
# O programa calcula as operações e imprime o resultado em um novo conjunto

def receber_arquivo(arquivo):
    with open(arquivo) as file:
        leitura = file.readlines()
    return leitura


def main():
    arquivo = input("Digite o nome do arquivo que você deseja testar, *utilize o .txt*: ")
    leitura = receber_arquivo(arquivo)
    
    quant_operacoes = int(leitura[0].strip())
    saidas = []
    
    for i in range(quant_operacoes):
        operacao = leitura[3 * i + 1].strip()
        conj1 = leitura[3 * i + 2].strip()
        conj2 = leitura[3 * i + 3].strip()
        
        nome, conj1, conj2, resultado = operacoes(operacao, conj1, conj2)
        saida = saida_lista(nome, conj1, conj2, resultado)
        saidas.append(saida)
        
    for saida in saidas:
        print(saida)

def operacoes(operacao, conj1, conj2):
    conj1 = set(conj1.split(", "))
    conj2 = set(conj2.split(", "))
    
    if operacao == 'U':
        resultado = conj1.union(conj2)
        nome = "união"
    elif operacao == "C":
        resultado = {(x, y) for x in conj1 for y in conj2}
        nome = "produto cartesiano"
    elif operacao == 'I':
        resultado = conj1.intersection(conj2)
        nome = "interseção"
    elif operacao == 'D':
        resultado = conj1.difference(conj2)
        nome = "diferença"

    return nome, conj1, conj2, resultado

def saida_lista(nome, conj1, conj2, resultado):
    conj1_lista = ', '.join(sorted(conj1))
    conj2_lista = ', '.join(sorted(conj2))
    
    if type(resultado) == set:
        resultado_formatado = ', '.join(sorted(map(str, resultado)))
    else:
        resultado_formatado = str(resultado)
    
    return f"{nome}: conjunto 1: {{{conj1_lista}}}, conjunto 2: {{{conj2_lista}}}, o resultado é: {{{resultado_formatado}}}."

if __name__ == "__main__":
    main()
