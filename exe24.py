# Número divisível por 2 e 3
def main():
    global n
    n = int(input("Insira um número: "))

    #chamada do módulo
    numeroDivisivel()

def numeroDivisivel():
    global n

    # inicio
    if n % 2 == 0 and n % 3 == 0:
        print(n, " é divisível por 2 e 3")
    elif n % 2 == 0:
        print(n, " só é dividível por 2")
    elif n % 3 == 0:
        print(n, " só é divisível por 3")
    else:
        print(n, " não é divisível por 2 e 3.")
    # fim
main()