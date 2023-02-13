import random

def erro(erros):
    print("    _______     ")
    print("   |/      |    ")

    if(erros == 1):
        print("   |     (º_º)   ")
        print("   |             ")
        print("   |             ")
        print("   |             ")

    if(erros == 2):
        print("   |     (º_º)   ")
        print("   |       |     ")
        print("   |             ")
        print("   |             ")

    if(erros == 3):
        print("   |     (º_º)   ")
        print("   |      /|     ")
        print("   |             ")
        print("   |             ")

    if(erros == 4):
        print("   |     (º_º)   ")
        print("   |      /|\    ")
        print("   |             ")
        print("   |             ")

    if(erros == 5):
        print("   |     (º_º)   ")
        print("   |      /|\    ")
        print("   |       |     ")
        print("   |             ")

    if(erros == 6):
        print("   |     (º_º)   ")
        print("   |      /|\    ")
        print("   |       |     ")
        print("   |      /      ")

    if (erros == 7):
        print("   |     (x_x)   ")
        print("   |      /|\    ")
        print("   |       |     ")
        print("   |      / \    ")

    print("   |              ")
    print("  _|___           ")
    print()
   

def checar(erros):
    if acertos == len(mylist):
        print("\nParabéns, você ganhou!")
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

        

    elif erros == 7:
        print("\nPuxa, você foi enforcado!")
        print("\nA palavra era {}".format(palavra))
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

opcao = 0

if opcao != 3:
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    erros = 0
    acertos = 0
    letras = []
    palavra = list(random.choice(open(r"C:\Users\User\Desktop\Jogo_Forca\palavras.txt").readline().split()))
    mylist = list(dict.fromkeys(palavra))
    print(palavra)

    while erros != 7 and acertos != len(mylist):
        
        tentativa = input("\nEscolha uma letra: ")

        while len(tentativa) > 1 or tentativa in letras:    
            tentativa = input("\nVocê digitou mais de uma letra ou digitou uma letra que já foi escolhida, escolha uma outra letra: ")


        letras.append(tentativa)

        if (tentativa in palavra):
            acertos += 1
            print("Acertou")

        else:
            erros += 1
            print("Errou!!")
            erro(erros)
        
       

        checar(erros)

        