from util import limpar_tela

def menu_principal():
    limpar_tela()
    print("___ MENU ___")
    print("1 - Cadastrar evento")
    print("2 - Listar eventos")
    print("3 - Alterar informações")
    print("4 - Remover")
    print("5 - Filtrar")
    print("6 - Vizualizar indicadores")
    print("0 - sair")
    opcao = ler_opcao(7)
    
    opcoes = {
        1: menu_cadastro(),
        2: menu_listar(),
        3: menu_alterar(),
        4: menu_remocao(),
        5: menu_filtros(),
        6: indicadores(),
        0: sair()
        }
        
    opcoes.get(opcao)
        
def menu_cadastro():
    pass 
def menu_listar():
    pass 
def menu_alterar():
    pass 
def menu_remocao():
    pass 
def menu_filtros():
    pass 
def indicadores():
    pass 
def sair():
    pass

def ler_opcao(qntd_opcoes): 
    try:
        opcao = int(input("Escolha uma opção: "))
        if 0<= opcao <=qntd_opcoes:
            return opcao
    except ValueError:
        pass
    print("Opção inválida! Aperte enter para avançar.")
    return -1
    

    
    