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
    
            
def remover_participante(indice):
    limpar_tela()
    for evento in eventos:
        participantes = evento.get('participantes', [])
    nome = participantes[indice]['nome']
    del participantes[indice]
    print(f"Participante '{nome}' removido com sucesso.")
    
    # encontrou_participante = False  

    # for evento in eventos:
    #     participantes = evento.get('participantes', [])
    #     if participantes:
    #         encontrou_participante = True
    #         print(f"\nEvento: {evento.get('nome', 'Sem nome')}")
    #         for participante in participantes:
    #             print(f"Nome: {participante.get('nome')}")
    #             print(f"CPF: {participante.get('cpf')}")
    #             print(f"Data de nascimento: {participante.get('data_nasc')}")
    #             print("-" * 30)

    # if not encontrou_participante:
    #     print("Nenhum participante cadastrado.")
        
    # input("\nAperte a tecla Enter para voltar")

def remover_participante_menu():   
    while True:
            print("___Qual participante deseja remover?___")
            print("1 - Voltar")
            print("2 - Sair")
            encontrou_participante = False  
            for evento in eventos:
                participantes = evento.get('participantes', [])
                if participantes:
                    encontrou_participante = True
                for i, item in enumerate(participantes, start=2):
                    print(f"{i} - {item['nome']}")
            if not encontrou_participante:
                print("Nenhum participante cadastrado.")
            input("\nAperte a tecla Enter para voltar")
            
            opcao = ler_opcao(len(eventos) + 3)

            if opcao == 1:
                break
            elif opcao == 2:
                sair()
            elif opcao == 3:
                sair()
            elif 4 <= opcao <= len(participantes) + 3:
                indice = opcao - 2
                remover_participante(indice)
            else:
                print("Opção inválida.")


