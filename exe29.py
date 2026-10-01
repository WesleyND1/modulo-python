# Receber  o tipo de investimento (1 = poupança, 2 = renda fixa)
# Calcular e mostrar o valor corrigido em 30 dias sabendo que:
# poupança = 3% e renda fixa = 5%, demais tipos não serão considerados.

# função calcular investimento
def invest(tipo,valor):

    if tipo == 1 :
        tipoPoupanca = valor * 0.03
        valorCorrigido = valor + tipoPoupanca
    elif tipo == 2 :
            tipoFixo = valor * 0.05
            valorCorrigido = valor + tipoFixo
    else:
        valorCorrigido = valor
        
    return valorCorrigido;

# Módulo principal
def main():
    print('Selecione o tipo de investimento, (poupança 1) ou (reda fixa 2):')
    n1 = int(input('Digite o tipo: '))
    valorInvestir = float(input('Insira o valor a investir: '))

    #chamada da função
    invest(n1,valorInvestir)
    print('Valor corrigido do investimento: R$',invest(n1,valorInvestir))

if (__name__ == '__main__'):
    main()