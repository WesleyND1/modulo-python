# Receber o preço atual e a média mensalde um produto
# calcular e exibir o novo preço

def calcularPreco(preco,mediaM):

    if mediaM < 500 and preco < 30:
        novoPreco = preco + (preco * 10 / 100)

    elif mediaM >= 500 and mediaM < 1000 and preco >= 30 and preco < 80:
        novoPreco = preco + (preco * 15 / 100)

    elif mediaM >= 1000 and preco >= 80:
        novoPreco = preco - (preco * 5 / 100)

    else:
        novoPreco = preco

    return novoPreco

def main():
    Pa = float(input('Digite o preço atual do produto: '))
    mediaMensal = float(input('Digite a média do produto: '))

    #chamada da função
    print('Preço novo é: ',calcularPreco(Pa, mediaMensal));

if (__name__ == '__main__'):
    main()