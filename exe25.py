# Calcular tempo do jogo
def main():
    global hora_inicio, min_inicio
    global hora_fim, min_fim

    hora_inicio = int(input("Hora de início: "))
    min_inicio = int(input("Minuto de início: "))

    hora_fim = int(input("Hora de final: "))
    min_fim = int(input("Minuto de final: "))

    #chamada do módulo
    calcTempJogo()

#Módulo para calcular tempo jogado
def calcTempJogo():
    global hora_inicio, min_inicio
    global hora_fim, min_fim
    
    inicio = hora_inicio * 60 + min_inicio
    fim = hora_fim * 60 + min_fim

    # inicio
    if fim <= inicio:
        fim += 24 * 60

    duracao = fim - inicio

    horas = duracao // 60
    minutos = duracao % 60

    print("Duração total:", horas, "hora(s) e", minutos, "minuto(s)")
    # fim

main()