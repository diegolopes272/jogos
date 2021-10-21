
#estudos python3 da Alura
#DFLL-set/2021

import forca
import adivinhacao

def escolha_jogo():
    print("********************************")
    print("******Escolha o seu jogo!!******")
    print("********************************")

    print("(1)->Forca    (2)->Adivinhação")

    jogo = int(input("Qual jogo vc quer?"))

    if(jogo == 1):
        print("Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Adivinhação")
        adivinhacao.jogar()

#para executar via terminal nos demais modulos
if(__name__ == "__main__"):
    escolha_jogo()




