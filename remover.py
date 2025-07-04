from util import limpar_tela
from evento_registro import eventos
from entrada import ler_opcao
from saida import sair 

def remover_evento():
    limpar_tela()
    while True:
        print(" ")
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
    
def remover_participante(opcao, lista):
    limpar_tela()
    evento, indice = lista[opcao - 3]
    nome = evento['participantes'][indice]['nome']
    del evento['participantes'][indice]
    print(f"Participante '{nome}' removido com sucesso.")
    print(" ")
    input("\nAperte Enter para continuar")

def remover_participante_menu():
    while True:
        limpar_tela()
        print("___Qual participante deseja remover?___")
        print("1 - Voltar")
        print("2 - Sair")
        lista_participantes = []
        contador = 3

        for evento in eventos:
            participantes = evento.get('participantes', [])
            for i, participante in enumerate(participantes):
                print(f"{contador} - {participante['nome']} (Evento: {evento['nome']})")
                lista_participantes.append((evento, i))
                contador += 1

        if not lista_participantes:
            print("Nenhum participante cadastrado.")
            input("Pressione Enter para voltar")
            break  

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida.")
            input("Pressione Enter para continuar")
            continue

        if opcao == 1:
            break
        elif opcao == 2:
            sair()
        elif 3 <= opcao < contador:
            remover_participante(opcao, lista_participantes)
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar")



