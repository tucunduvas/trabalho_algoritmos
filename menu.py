from util import limpar_tela
from evento_registro import cadastrar_evento
from listar import listar_evento
from listar import listar_participantes
import alterar as a
from remover import remover_participante_menu
from entrada import ler_opcao
from saida import sair
from remover import remover_evento
from filtro import menu_mes
from filtro import menu_geracoes
from indicadores import mostrar_indicadores
from participantes import cadastrar_participante_evento
from evento_registro import eventos

def menu_principal():
    while True:
        limpar_tela()
        print("___ MENU ___")
        print("1 - Cadastrar evento e participantes")
        print("2 - Listar eventos")
        print("3 - Alterar informações")
        print("4 - Remover")
        print("5 - Filtrar")
        print("6 - Visualizar indicadores")
        print("0 - Sair")
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
        print(" 2 - Cadastrar participante em evento existente")
        print(" 3 - Voltar")
        opcao = ler_opcao(3)
        
        opcoes = {
            1: cadastrar_evento,
            2: lambda: cadastrar_participante_evento(eventos),
            3: None,
        }
        
        if opcao == 3:
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
    print("2 - Voltar")
    opcao = ler_opcao(2)
    
    opcoes = {
        1: a.alterar_evento,
        2: None
    }
    
    if opcoes.get(opcao):
        opcoes[opcao]()
    
    
def menu_remocao():
    limpar_tela()
    print("__Remover__")
    print("1 - Remover participante")
    print("2 - Remover eventos")
    print("4 - Voltar")
    opcao = ler_opcao(3)
    
    opcoes = {
        1: remover_participante_menu,
        2: remover_evento,
        4: None
    }
    
    if opcoes.get(opcao):
        opcoes[opcao]()
    
def menu_filtros():
    limpar_tela()
    print("__Filtros__")
    print("1 - Filtrar os eventos por mês")
    print("2 - Filtrar os participantes por geração")
    print("3 - Voltar")
    opcao = ler_opcao(5)
    
    opcoes = {
        1: menu_mes,
        2: menu_geracoes,
        3: None
    }
    
    if opcoes.get(opcao):
        opcoes[opcao]()

def indicadores():
    limpar_tela()
    mostrar_indicadores()



    
    