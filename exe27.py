# Função para calcular velocidade média
def velocidadeMedia(voltas,extensao,tempo):
    #variáveis locais
    tempo = tempo / 60
    distancia = (voltas * extensao) / 1000
    Vmedia = distancia / tempo
    return Vmedia


def main():
    
    nVoltas = float(input('Digite o número de voltas: '))
    extensaoC = float(input('Isira a extensão do circuito (em metros): '))
    tempD = float(input('Digite o tempo de duração (em minutos): '))

    #chamada da funcão com parâmetro
    resultado = velocidadeMedia(nVoltas,extensaoC,tempD)
    print(resultado)


if (__name__ == '__main__'):
    main()