def ler_opcao(qntd_opcoes): 
    try:
        opcao = int(input("Escolha uma opção: "))
        if 0<= opcao <=qntd_opcoes:
            return opcao
    except ValueError:
        pass
    print("Opção inválida! Aperte enter para avançar.")

    