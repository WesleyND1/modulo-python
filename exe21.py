# Calcular se aluno foi aprovado ou não.
#modulo principal
def main():
    # Declarar variáveis
    global n1, n2, n3, n4

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))

    #chamada do módulo
    mediaAluno()

#modulo calcular média
def mediaAluno():
    global n1, n2, n3, n4

    media = (n1 + n2 + n3 + n4) / 4

    # Estrutura encadeada
    if media >= 6 :
        print("Aluno aprovado")
    elif media >= 3 :
        print("Aluno em exame")
    else:
        print("Aluno reprovado")
    # Fim

main()