
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
            input("\nAperte a tecla Enter para voltar")
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
    eventos_filtro = list(filter(lambda e: datetime.strptime(e['data'], "%d/%m/%Y").month == mes, eventos))
    if not eventos_filtro:
        print("Nenhum evento encontrado no mês.")
        input("Pressione a tecla Enter para retornar.")
    else:
        for evento in eventos_filtro:
            print(f"Nome: {evento['nome']} | Data: {evento['data']}")
        input("Pressione a tecla Enter para retornar.")

def menu_geracoes():
    while True: 
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
        
        if opcoes.get(opcao):
            opcoes[opcao]()
    


todos_participantes = []
for evento in eventos:
    todos_participantes.extend(evento['participantes'])

def genz():
    participantes_genz = list(filter(lambda p: 1997<=datetime.strptime(p['data_nasc'], "%d/%m/%Y").year<=2012, todos_participantes))
    for p in participantes_genz:
        print(p['nome'])
    
    
def genx():
    participantes_genx = list(filter(lambda p: 1965<=datetime.strptime(p['data_nasc'], "%d/%m/%Y").year<=1980, todos_participantes))
    for p in participantes_genx:
        print(p['nome'])

def alpha():
    participantes_alpha = list(filter(lambda p: 2012<datetime.strptime(p['data_nasc'], "%d/%m/%Y").year, todos_participantes))
    for p in participantes_alpha:
        print(p['nome'])


def millenials():
    participantes_millenials = list(filter(lambda p: 1981<=datetime.strptime(p['data_nasc'], "%d/%m/%Y").year<=1996, todos_participantes))
    for p in participantes_millenials:
        print(p['nome'])
    
def babyboomers():
    participantes_babyboomers = list(filter(lambda p: 1946<=datetime.strptime(p['data_nasc'], "%d/%m/%Y").year<=1964, todos_participantes))
    for p in participantes_babyboomers:
        print(p['nome'])
    

