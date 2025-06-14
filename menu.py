from util import limpar_tela
from evento_registro import cadastrar_evento
from listar import listar_evento
from listar import listar_participantes
from alterar import alterar_participante
from alterar import alterar_evento
from remover import remover_evento 
from remover import remover_participante
from filtro import filtro_tema
from filtro import filtro_mes
from filtro import filtro_qntd_participantes
from filtro import filtro_idade
from entrada import ler_opcao
from saida import sair

def menu_principal():
    while True:
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
            1: menu_cadastro,
            2: menu_listar,
            3: menu_alterar,
            4: menu_remocao,
            5: menu_filtros,
            6: indicadores,
            0: sair
            }
            
        if opcoes.get(opcao):
            opcoes[opcao]()

        
def menu_cadastro():
    while True:
        limpar_tela()
        print("__ Cadastrar __")
        print(" 1 - Cadastrar evento")
        print(" 2 - Voltar")
        opcao = ler_opcao(2)
        
        opcoes = {
            1: cadastrar_evento,
            2: None,
        }
        
        if opcao == 2:
            break
        
        if opcoes.get(opcao):
            opcoes[opcao]()
    
def menu_listar():
    limpar_tela()
    print("__Listar__")
    print("1 - Ver informações de eventos")
    print("2 - Ver lista completa de participantes")
    print("3 - Voltar")
    opcao = ler_opcao(3)
    
    opcoes = {
        1: listar_evento,
        2: listar_participantes,
        3: None
    }
    
    if opcoes.get(opcao):
        opcoes[opcao]()
    
    
def menu_alterar():
    limpar_tela()
    print("__Alterações__")
    print("1 - Alterar dados de um evento")
    print("2 - Alterar dados de um participante")
    print("3 - Voltar")
    opcao = ler_opcao(3)
    
    opcoes = {
        1: alterar_evento,
        2: alterar_participante,
        3: None
    }
    
    if opcoes.get(opcao):
        opcoes[opcao]()
    
    
def menu_remocao():
    limpar_tela()
    print("__Remover__")
    print("1 - Remover participante")
    print("2 - Remover evento")
    print("3 - Voltar")
    opcao = ler_opcao(3)
    
    opcoes = {
        1: remover_participante,
        2: remover_evento,
        3: None
    }
    
    if opcoes.get(opcao):
        opcoes[opcao]()
    
def menu_filtros():
    limpar_tela()
    print("__Filtros__")
    print("1 - Filtrar os eventos por tema")
    print("2 - Filtrar os eventos por mês")
    print("3 - Filtrar os eventos por quantidade de participantes")
    print("4 - Filtrar os participantes por idade")
    print("5 - Voltar")
    opcao = ler_opcao(5)
    
    opcoes = {
        1: filtro_tema,
        2: filtro_mes,
        3: filtro_qntd_participantes,
        4: filtro_idade,
        5: None
    }
    
    if opcoes.get(opcao):
        opcoes[opcao]()
    
def indicadores():
    pass 




    
    