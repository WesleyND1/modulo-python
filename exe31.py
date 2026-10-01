# Função que calcula o fatorial
def CalcularFatorial(n):
    fatorial = 1
    i = n

    while i > 1:
        fatorial = fatorial * i
        i = i - 1

    return fatorial


# Função que recebe 2 parâmetros e retorna a divisão
def Dividir(num1, num2):
    return num1 / num2


def main():

    num = int(input('Digite um valor valor: '))

    serie = 0
    i = 0

    while i <= num:
        fatorial = CalcularFatorial(i)
        serie = serie + Dividir(1, fatorial)
        i = i + 1

    print('Resultado da série:', serie)


if __name__ == '__main__':
    main()