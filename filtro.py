
from datetime import datetime
from evento_registro import eventos
from saida import sair
from entrada import ler_opcao
from util import limpar_tela

def menu_mes():
    while True:
        limpar_tela()
        
        if not eventos:
            print("Nenhum evento cadastrado.")
            input("Pressione a tecla Enter para retornar")
            return

        print("Deseja ver os eventos de qual mês?")
        print("1 - Janeiro")
        print("2 - Fevereiro")
        print("3 - Março")
        print("4 - Abril")
        print("5 - Maio")
        print("6 - Junho")
        print("7 - Julho")
        print("8 - Agosto")
        print("9 - Setembro")
        print("10 - Outubro")
        print("11 - Novembro")
        print("12 - Dezembro")
        print("13 - Voltar")
        print("14 - Sair")
        opcao = ler_opcao(14)
        
        if opcao == 13:
            return
        elif opcao == 14:
            sair()
        else:
            eventos_do_mes(opcao)
        
def eventos_do_mes(mes):
    limpar_tela()
    eventos_filtro = list(filter(lambda e: datetime.strptime(e['data'], "%d/%m/%Y").month == mes, eventos))
    if not eventos_filtro:
        print("Nenhum evento encontrado no mês.")
        input("Pressione a tecla Enter para retornar.")
    else:
        for evento in eventos_filtro:
            print(f"Nome: {evento['nome']} | Data: {evento['data']}")
        input("Pressione a tecla Enter para retornar.")

todos_participantes = []
for evento in eventos:
    todos_participantes.extend(evento['participantes'])
    
def menu_geracoes():
    while True: 
        limpar_tela()
        if not todos_participantes:
            print("Nenhum participante cadastrado.")
            input("Pressione a tecla Enter para retornar")
            return
            
        print("Deseja ver os participantes de qual geração?")
        print(" 1 - Baby Boomers - Nascidos entre 1946 e 1964")
        print(" 2 - Geração X - Nascidos entre 1965 e 1980")
        print(" 3 - Millennials - Nascidos entre 1981 e 1996")
        print(" 4 - Geração Z - Nascidos entre 1997 e 2012")
        print(" 5 - Geração Alpha - Nascidos a partir de 2013")
        print(" 6 - Voltar")
        print(" 7 - Sair")
        opcao = ler_opcao(7)
        
        opcoes = {
            1: babyboomers,
            2: genx,
            3: millenials,
            4: genz,
            5: alpha,
            6: None,
            7: sair, 
        }
        if opcao == 6:
            break
        
        if opcoes.get(opcao):
            opcoes[opcao]()
    

def genz():
    limpar_tela()
    participantes_genz = list(filter(lambda p: 1997<=datetime.strptime(p['data_nasc'], "%d/%m/%Y").year<=2012, todos_participantes))
    if not participantes_genz: 
        print("Nenhum participante da geração Z encontrado.")
        input("Pressione a tecla Enter para retornar.")
    else: 
        print("Participantes Geração Z")
        for p in participantes_genz:
            print(f"{p['nome']} | {p['data_nasc']} | {p['evento_cadastrado']}" )
        input("Pressione a tecla Enter para retornar.")
    
def genx():
    limpar_tela()
    participantes_genx = list(filter(lambda p: 1965<=datetime.strptime(p['data_nasc'], "%d/%m/%Y").year<=1980, todos_participantes))
    if not participantes_genx: 
        print("Nenhum participante da geração X encontrado.")
        input("Pressione a tecla Enter para retornar.")
    else:
        print("Participantes Geração X")
        for p in participantes_genx:
            print(f"{p['nome']} | {p['data_nasc']} | {p['evento_cadastrado']}" )
        input("Pressione a tecla Enter para retornar.")

def alpha():
    limpar_tela()
    participantes_alpha = list(filter(lambda p: 2012<datetime.strptime(p['data_nasc'], "%d/%m/%Y").year, todos_participantes))
    if not participantes_alpha: 
        print("Nenhum participante da Geração Alpha encontrado.")
        input("Pressione a tecla Enter para retornar.")
    else:
        print("Participantes Alpha")
        for p in participantes_alpha:
            print(f"{p['nome']} | {p['data_nasc']} | {p['evento_cadastrado']}" )
        input("Pressione a tecla Enter para retornar.")
    

def millenials():
    limpar_tela()
    participantes_millenials = list(filter(lambda p: 1981<=datetime.strptime(p['data_nasc'], "%d/%m/%Y").year<=1996, todos_participantes))
    if not participantes_millenials: 
        print("Nenhum participante da geração Millenials encontrado.")
        input("Pressione a tecla Enter para retornar.")
    else:
        print("Participantes Millenials ")
        for p in participantes_millenials:
            print(f"{p['nome']} | {p['data_nasc']} | {p['evento_cadastrado']}" )
        input("Pressione a tecla Enter para retornar.")
    
def babyboomers():
    limpar_tela()
    participantes_babyboomers = list(filter(lambda p: 1946<=datetime.strptime(p['data_nasc'], "%d/%m/%Y").year<=1964, todos_participantes))
    if not participantes_babyboomers: 
        print("Nenhum participante da geração Baby Boomers encontrado.")
        input("Pressione a tecla Enter para retornar.")
    else:
        print("Participantes Baby Boomers")
        for p in participantes_babyboomers:
            print(f"{p['nome']} | {p['data_nasc']} | {p['evento_cadastrado']}" )
        input("Pressione a tecla Enter para retornar.")
    

