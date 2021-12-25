import random
import os

def menu_opcoes():
    print("[1] - Ver pontos ganhos.\n")
    print("[Y/N] - Você gostaria de jogar o dado? Digite Y/N..\n")

def explicacao():
    print("Você começa o jogo com '3' pontos, se perder tudo é game over. =(\n")
    print("Para cada erro você perde a quantidade de pontos apostada, para os acertos você ganha 1 ponto.\n")
    print("Você pode ganhar infinitos pontos.\n")
# menu
menu = True
pontos = 3
while menu is True:
    menu_opcoes()
    # Verificando se o usuario gostaria de jogar.
    jogar = str(input())
    if jogar.upper() == "Y":
        #começando jogo
        print("\n" * os.get_terminal_size().lines)
        explicacao()
        # Perguntando aposta
        aposta = int(input("Quantos pontos você gostaria de apostar?\n"))
        if aposta > pontos or aposta < 0:
            print("\n" * os.get_terminal_size().lines)
            print("Você não tem esses pontos!\n")
        # Perguntando palpite
        else:
            palpite = int(input("Digite seu palpite.\n"))
            # lançando dado
            dado = random.randint(1,2)
            # Acerto ou erro
            if palpite == dado:
                print("Você Acertou!\n")
                print(f"O dado caio no numero {dado:.0f}")
                pontos = pontos + 1
                print(f"Você ganhou 1 ponto\n total: {pontos}")
            else:
                print("Você Errou!\n")
                print(f"O dado caiu no numero {dado:.0f}")
                pontos = pontos - aposta
                print(f"Você perdeu 1 ponto\n total: {pontos}")
        # Game Over
        if pontos == 0:
            print("\n" * os.get_terminal_size().lines)
            print("GAME OVER!")
            resposta = int(input("digite [5] para jogar novamente\nDigite [8] para sair do jogo.\n"))
            if resposta == 5:
                pontos = 3
            elif resposta == 8:
                print("Saindo do jogo!")
                menu = False
            else:
                print("Digite uma opção Valida!")
    # jogo não começa
    elif jogar.upper() == "N":
        print("\n" * os.get_terminal_size().lines)
        print("Uma pena, poderia ter nos divertido com as apostas. =)\n")
        menu = False
    elif jogar == "1":
        print("\n" * os.get_terminal_size().lines)
        print(f"Você tem {pontos:.0f} pontos.\n\n")
    else:
        print("digite uma opção Valida!\n")
    