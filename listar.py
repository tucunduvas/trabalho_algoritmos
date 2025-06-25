from evento_registro import eventos
from entrada import ler_opcao
from saida import sair
from util import limpar_tela


def listar_evento():
    limpar_tela()
    while True:
        print("___Qual evento deseja listar?___")
        print("1 - Todos")
        print("2 - Voltar")
        print("3 - Sair")
        i = 3
        for i,item in enumerate(eventos, start=4):
            print(f"{i} - {item['nome']}")
        opcao = ler_opcao(len(eventos)+3)
        
        opcoes = {
            1: listar_todos_eventos, 
            2: None,
            3: sair,
            }
        
        if opcao == 2:
            break
        
        if opcao >=3 and opcao<=len(eventos)+3:
            listar_evento_especifico(eventos[opcao - 3])

        if opcoes.get(opcao):
                opcoes[opcao]()
        

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
    print("__Participantes__")
    participantes = evento.get('participantes', [])
    if participantes:
        for participante in participantes:
            print(f"Nome: {participante.get('nome')}")
            print(f"CPF: {participante.get('cpf')}")
            print(f"Data de nascimento: {participante.get('data_nasc')}")
            

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
    for i in eventos:
        participantes = i.get('participantes', [])
        if participantes:
            for participante in participantes: 
                print(f"Nome: {participante.get('nome')}")
                print(f"CPF: {participante.get('cpf')}")
                print(f"Data de nascimento: {participante.get('data_nasc')}")


