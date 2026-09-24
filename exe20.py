# Equação do 2º grau, calcule e mostre.
import math


def main():
    # Declarar variáveis
    global a, b, c

    # Receber dados
    a = float(input("Digite o coeficiente A: "))
    b = float(input("Digite o coeficiente B: "))
    c = float(input("Digite o coeficiente C: "))

    # Chamada do módulo
    equacao()


def equacao():
    global a, b, c

    delta = b**2 - 4 * a * c

    if delta < 0:
        print("Não existem raízes reais.")

    elif delta == 0:
        x = -b / (2 * a)
        print("Existe uma raiz real:", x)

    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        print("X1:", x1)
        print("X2:", x2)

main()