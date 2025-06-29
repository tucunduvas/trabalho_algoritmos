
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


todos_participantes = []
for evento in eventos:
    todos_participantes.extend(evento['participantes'])

def genz(participante):
    data_nasc = datetime.strptime(participante['data_nasc'], "%d/%m/%Y")
    return 2012>=data_nasc.year >= 1997


participantes_genz = list(filter(genz, todos_participantes))

for _ in participantes_genz:
    print(_['nome'])
    
    
def genx(participante):
    data_nasc = datetime.strptime(participante['data_nasc'], "%d/%m/%Y")
    return 1965<=data_nasc.year<=1980


participantes_genx = list(filter(genx, todos_participantes))

for _ in participantes_genx:
    print(_['nome'])
    
def millenials(participante):
    data_nasc = datetime.strptime(participante['data_nasc'], "%d/%m/%Y")
    return 1981<=data_nasc.year<=1996


participantes_millenials = list(filter(millenials, todos_participantes))

for _ in participantes_millenials:
    print(_['nome'])
    
    
def babyboomers(participante):
    data_nasc = datetime.strptime(participante['data_nasc'], "%d/%m/%Y")
    return 1946<=data_nasc.year<=1964


participantes_babyboomers = list(filter(babyboomers, todos_participantes))

for _ in participantes_babyboomers:
    print(_['nome'])
    

