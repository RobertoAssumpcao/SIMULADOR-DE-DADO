import random
# menu
menu = True
while menu is True:

    # Verificando se o usuario gostaria de jogar.
    jogar = str(input("Você gostaria de jogar o dado? Digite Y/N\n")) #tratar erro
    if jogar.upper() == "Y":
        dado = random.randint(1,6)
        print(f'O numero do dado foi {dado:.0f}')
    # jogo não começa
    elif jogar.upper() == "N":
        print("Uma pena, poderia ter nos divertido com as apostas =)\n")
        menu = False
    else:
        print("digite uma opção Valida!\n")
    