# Diferença do maior pelo menor em módulo

def main():
    #declarar variáveis globais
    global n1, n2, diferenca

    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))

    #chamada do módulo
    diferenca()

#módulo verificar diferença dos valores
def diferenca():

    global n1, n2, diferenca

    if n1 > n2:
        diferenca = n1 - n2
    else:
        diferenca = n2 - n1

    print("Diferença:", diferenca)


main()