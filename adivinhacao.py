
import random

def jogar():

    print("********************************")
    print("Bem vindo no jogo de adivinhação")
    print("********************************")

    #numero_secreto = round((random.random() * 100)) #random gera entre 0.0 e 1.0
    numero_secreto = random.randrange(1,101)    #range de 1 a 100 - inclui 100
    #print("Debug Secreto {}".format(numero_secreto))

    #variaveis do jogo
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1) facil  (2) medio  (3) treta")

    nivel = int(input("defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #range até limite superior
    for rodada in range(1, total_de_tentativas + 1):
        print("Rodada {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite um numero de 1 a 100: ")
        chute = int(chute)
        print("Voce digitou: ", chute)

        if(chute < 1 or chute > 100):
            print("Voce deve entrar com valor entre 1 e 100 jovem!!")
            continue

        acertou = numero_secreto == chute
        maior = numero_secreto < chute
        menor = numero_secreto > chute

        if(acertou):
            print("voce acertou maoeee!!!!")
            break
        else:
            if(maior):
                print("Errrroooouuuu pra cima")
            elif(menor):
                print("Errrroooouuuu pra baixo")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = (pontos - pontos_perdidos)

    if(acertou):
        print("Parabens!!!", "Pontos:{}".format(pontos))
    else:
        print("Game Over!!")


if(__name__ == "__main__"):
    jogar()