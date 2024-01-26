import forca
import adivinhacao

def escolhe_jogo():
    
    #Definição das variáveis
    jogo = 100

    while(jogo != 1 or jogo != 2 or jogo!= 0):

        print("*********************************")
        print("*******Escolha o seu jogo!*******")
        print("*********************************")

        print("(1) Forca (2) Adivinhação (0) SAIR")

        jogo = int(input("Qual jogo? "))

        if(jogo == 1):
            print("Jogando forca")
            forca.jogar()
        elif(jogo == 2):
            print("Jogando adivinhação")
            adivinhacao.jogar()
        elif(jogo == 0):
            print("Obrigado e até a próxima!!!")
            break
        else:
            print("Escolha o número de um jogo disponível ou 0 para sair.")
            

if(__name__ == "__main__"):
    escolhe_jogo()
