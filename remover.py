from util import limpar_tela
from evento_registro import eventos
from entrada import ler_opcao
from saida import sair 

def remover_evento():
    limpar_tela()
    while True:
        print("___Qual evento deseja remover?___")
        print("1 - Todos")
        print("2 - Voltar")
        print("3 - Sair")
        for i, item in enumerate(eventos, start=4):
            print(f"{i} - {item['nome']}")
        
        opcao = ler_opcao(len(eventos) + 3)

        if opcao == 1:
            remover_todos_eventos()
        elif opcao == 2:
            break
        elif opcao == 3:
            sair()
        elif 4 <= opcao <= len(eventos) + 3:
            indice = opcao - 4
            remover_evento_especifico(indice)
        else:
            print("Opção inválida.")

def remover_todos_eventos():
    eventos.clear()
    print("Todos os eventos foram removidos!")

def remover_evento_especifico(indice):
    nome = eventos[indice]['nome']
    del eventos[indice]
    print(f"Evento '{nome}' removido com sucesso.")
    
def remover_participante():
    pass
