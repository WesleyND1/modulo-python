# Dois valores em ordem crescente

def main():
    global n1, n2

    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))

    #chamada do módulo
    ordemC()

def ordemC():
    global n1, n2

    # Inicio
    if n1 < n2:
        print(n1, n2)
    else:
        print(n2, n1)
    # Fim
main()