# Receber um número e exibir seu fatorial através de função

#função fatorial
def CalcularFatorial(n):
    #variavel local
    fatorial = 1
    i = n

    #laço enquanto
    while i > 1:
        fatorial = fatorial * i 
        i = i - 1
    return fatorial

# Módulo principal
def main():
    num = int(input('Digite um número para ver seu fatorial: '))

    #chamada da função
    CalcularFatorial(num)
    print(CalcularFatorial(num))


if (__name__ == '__main__'):
    main()