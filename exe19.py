# Maior entre os valores com Módulo

def main():
    global n1, n2

    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))

    #chamada do módulo
    maiorValor()


#módulo para verificar e exibir o maior valor
def maiorValor():
    global n1,n2

    # Inicio
    if n1 > n2:
        print("Maior:", n1)
    else:
        print("Maior:", n2)
    # Fim
main()