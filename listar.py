from eventoos import eventos
from eventoos import evento
from menu import ler_opcao
from menu import menu_listar
from menu import sair

"""
def menu_listar():
    print("__Listar__")
    print(" 1 - Ver informações de eventos")
    print("2 - Ver lista completa de participantes")
    print("3- Ver informações de um único participante")
    print("4 - Voltar")
    opcao = ler_opcao(4)
    
"""

def listar_evento():
    print("___Qual evento deseja listar?___")
    print("1 - Todos")
    print("2 - Voltar")
    print("3 - Sair")
    i = 3
    for item in eventos:
        i+= 3
        print(f"{i} - {item['nome']}")
    opcao = ler_opcao(len(eventos)+3)
    #duvida 
    opcoes = {
        1: listar_todos_eventos, 
        2: menu_listar,
        3: sair,
        
        }
        
    opcoes.get(opcao)
    
def listar_todos_eventos():
    for item in eventos:
        print(f"Id: {item['id']}")
        print(f"Nome: {item['nome']}")
        print(f"Data: {item['data']}")
        print(f"Endereço: {item['endereço']}")
        print(listar_participantes())
def listar_participante():
    pass

def listar_participantes():
    pass

