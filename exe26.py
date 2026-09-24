# Verificar se maior é múltiplo do menor

def main():
    global n1, n2

    n1 = int(input("Insira um número: "))
    n2 = int(input("Insira o segundo número: "))

    #chamada do módulo
    multiplo()

def multiplo():
    global n1, n2

    #condicional composta
    if n1 > n2:
        menor = n2
        maior = n1
    else:
        menor = n1
        maior = n2

    if maior % menor == 0:
        print("Maior é múltiplo de", menor)
    else:
        print("Maior não é múltiplo de", menor)

main()