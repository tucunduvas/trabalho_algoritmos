def ler_opcao(qntd_opcoes): 
    while True: 
        try:
            opcao = int(input("Escolha uma opção: "))
            if 0<= opcao <=qntd_opcoes:
                return opcao
        except ValueError:
            pass
        print("Opção inválida! Tente novamente.")

    