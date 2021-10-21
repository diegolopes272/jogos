
import random

def jogar():
    imprimi_msg_abertura()

    palavra_secreta = carrega_palavra_secreta()

    enforcou = False
    acertou = False
    erros = 0
    max_erros = 7

    #letras_acertadas = ["_","_","_","_","_","_"]
    letras_acertadas  = inicializa_letras_acertadas(palavra_secreta)

    while(not enforcou and not acertou):
        print("Soletrando...")
        print(letras_acertadas)
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Errrrrouuuu.. faltam {} tentativas".format(max_erros - erros))
            desenha_forca(erros)

        enforcou = erros >= max_erros
        acertou = "_" not in letras_acertadas

    if(enforcou):
        imprime_msg_perdedor(palavra_secreta)
    else:
        imprime_msg_vencedor(letras_acertadas)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_msg_perdedor(palavra_secreta):
    print("Game Over !!!!!!!!!!")
    print("A palavra secreta era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_msg_vencedor(letras_acertadas):
    print(letras_acertadas)
    print("Parabens ganhou um milhaooo!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprimi_msg_abertura():
    print("********************************")
    print("***Bem vindo no jogo de forca**")
    print("********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    # print(palavras)

    numero = random.randrange(0, len(palavras))

    # palavra_secreta = "banana".upper()
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for i in palavra]

def pede_chute():
    chute = input("Qual letra?: ")
    chute = chute.strip().upper()
    return chute


#para chamar automatico se quiser diretamente
if(__name__ == "__main__"):
    jogar()
