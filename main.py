# Verificando se o usuario gostaria de jogar.
jogar = input("Você gostaria de jogar o dado? Digite Y/N\n") #tratar erro
if jogar.upper() == "Y":
    
  """  # Começando jogo.
    comeca_jogo = True
    while comeca_jogo is True:
        

        #verificando se o usuario gostaria de sair do jogo.
        print("Digite '1' para continuar.\n")
        print("Digite '0' para sair.\n")
        continua_jogo = int(input("Qual sua resposta ?\n")) #tratar erro

        # Jogo continua
        if continua_jogo == 1:
            comeca_jogo = True
        # jogo acaba
        elif continua_jogo == 0:
            comeca_jogo = False
            print("Saindo do jogo!")
        # Tratando erro
        else:
            print("Digite uma opção valida")
"""
# jogo não começa
else:
    print("Uma pena, poderia ter nos divertido com as apostas =)\n")