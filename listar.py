from evento_registro import eventos
from entrada import ler_opcao
from saida import sair
from util import limpar_tela


def listar_evento():
    limpar_tela()

    if not eventos:
        print("Nenhum evento cadastrado.")
        input("\nAperte a tecla Enter para voltar")
        return

    while True:
        print("___Qual evento deseja listar?___")
        print("1 - Todos")
        print("2 - Voltar")
        print("3 - Sair")
        i = 3
        for i,item in enumerate(eventos, start=4):
            print(f"{i} - {item['nome']}")
        opcao = ler_opcao(len(eventos)+3)
        
        if opcao == 1:
            listar_todos_eventos()
        elif opcao == 2:
            break
        elif opcao == 3:
            sair()
        elif 4 <= opcao <= len(eventos) + 3:
            indice = opcao - 4
            listar_evento_especifico(eventos[indice])
        else:
            print("Opção inválida.")
        

def listar_evento_especifico(evento):
    limpar_tela()
    print(f"ID: {evento['id']}")
    print(f"Nome: {evento['nome']}")
    print(f"Nome: {evento['nome']}")
    print(f"Data: {evento['data']}")
    endereco = evento.get('endereço')
    if endereco:
        print(f"Rua: {endereco.get('rua')}")
        print(f"Bairro: {endereco.get('bairro')}")
        print(f"CEP: {endereco.get('cep')}")
        print("-" * 30)
    print("Participantes")
    participantes = evento.get('participantes', [])
    if participantes:
        for participante in participantes:
            print(f"Nome: {participante.get('nome')}")
            print(f"CPF: {participante.get('cpf')}")
            print(f"Data de nascimento: {participante.get('data_nasc')}")
            print("-" * 30)

            

def listar_todos_eventos():
    limpar_tela()
    for i,item in enumerate(eventos):
        print("__Evento {i}__")
        print(f"Id: {item['id']}")
        print(f"Nome: {item['nome']}")
        print(f"Data: {item['data']}")
        endereco = item.get('endereço')
        if endereco:
            print(f"Rua: {endereco.get('rua')}")
            print(f"Bairro: {endereco.get('bairro')}")
            print(f"CEP: {endereco.get('cep')}")
        print("__Participantes__")
        participantes = item.get('participantes', [])
        if participantes:
            for participante in participantes: 
                print(f"Nome: {participante.get('nome')}")
                print(f"CPF: {participante.get('cpf')}")
                print(f"Data de nascimento: {participante.get('data_nasc')}")
            
def listar_participantes():
    limpar_tela()
    encontrou_participante = False  

    for evento in eventos:
        participantes = evento.get('participantes', [])
        if participantes:
            encontrou_participante = True
            print(f"\nEvento: {evento.get('nome', 'Sem nome')}")
            for participante in participantes:
                print(f"Nome: {participante.get('nome')}")
                print(f"CPF: {participante.get('cpf')}")
                print(f"Data de nascimento: {participante.get('data_nasc')}")
                print("-" * 30)

    if not encontrou_participante:
        print("Nenhum participante cadastrado.")
        
    input("\nAperte a tecla Enter para voltar")
