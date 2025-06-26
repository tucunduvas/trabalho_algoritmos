from util import limpar_tela
from evento_registro import eventos
from entrada import ler_opcao
from saida import sair 

def remover_evento_especifico():
    limpar_tela()
    while True:
        print("___Qual evento deseja remover?___")
        print("1 - Todos")
        print("2 - Voltar")
        print("3 - Sair")
        i = 3
        for i,item in enumerate(eventos, start=4):
            print(f"{i} - {item['nome']}")
        opcao = ler_opcao(len(eventos)+3)
        
        opcoes = {
            1: remover_todos_eventos, 
            2: None,
            3: sair,
            }
        
        if opcao == 2:
            break
        
        if opcao >=3 and opcao<=len(eventos)+3:
            remover_evento_especifico(eventos[opcao - 4])
    
        if opcoes.get(opcao):
                opcoes[opcao]()
        
        del eventos[opcao]
        
def remover_todos_eventos():
    eventos.clear()
    print("Eventos removidos!")
    

def remover_evento_especifico(evento_escolhido):
    del 

def remover_participante():
    pass 

# se o evento tiver se 1 participante 