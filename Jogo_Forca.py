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
    if len(letra_palavra) == 0:
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
        string = "".join(str(x) for x in palavra)
        print("Você foi enforcado! A palavra era " + string)



opcao = 0

while opcao != 2:
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    erros = 0
    letras = []
    palavra = random.choice(open(r"C:\Users\User\Desktop\Jogo_Forca\palavras.txt").readline().split())
    letra_palavra = set(palavra)
    letras_acertadas = ["_"] * len(palavra)
    print(palavra)
    
    
    while erros != 7 and len(letra_palavra) != 0:
       
        print("\nPalavra:", end=" ")
        for tentativa in letras_acertadas:
                print(tentativa, end=" ")

        print("\n")

        tentativa = input("Escolha uma letra: ")

        while len(tentativa) > 1 or tentativa in letras:    
            tentativa = input("Você digitou mais de uma letra ou digitou uma letra que já foi escolhida, escolha uma outra letra: ")
        

        letras.append(tentativa)

        if (tentativa in palavra):
            print("Acertou")
            letra_palavra.remove(tentativa)
            for i in range(len(palavra)):
                    if palavra[i] == tentativa:
                        letras_acertadas[i] = tentativa
            
        else:
            erros += 1
            print("Errou!!")
            erro(erros)
        

        checar(erros)


    while True:
        print("\nDigite 1 caso queira rejogar.\nDigite 2 caso queira sair.")
        opcao = int(input(">>> "))

        if opcao == 1:
            print("\nReiniciando....")
            break
        elif opcao == 2:
            print("\nSaindo.......")
            break
        else:
            print("\nOpção inválida, por favor digite novamente.")

    
   