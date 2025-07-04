import datetime
import uuid
from entrada import ler_opcao

def cadastrar_participantes(nome_evento):
    participante = {
        'id':  f"p{uuid.uuid4()}",
        'nome': input("Digite o nome do participante: "),
        'cpf':  validacao_cpf(),
        'data_nasc': validacao_datanasc(),
        'evento_cadastrado': nome_evento
    }
    return participante

def validacao_datanasc():
    data_nascimento = input(("Digite a data de nascimento do participante, no formato dia/mes/ano e com apenas números: "))
    try: 
        datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
        return data_nascimento
    except ValueError:
        print("Inválido! O campo data de nascimento aceita apenas numeros no formato dia/mês/ano, tente novamente!")



def validacao_cpf():
    cpf = input(("Digite  o cpf do participante, com apenas números: "))
    try: 
        if len(cpf)==11:
            return cpf
    except ValueError:
        print("Inválido! O campo cpf aceita apenas números, tente novamente!")



def cadastrar_participante_evento(eventos):
    print(" ")
    print("Eventos disponíveis:")
    for indice, evento in enumerate(eventos):
        print(f"{indice +1} - {evento['nome']}")

    opcao = ler_opcao(len(eventos))
    evento = eventos[opcao - 1]
    nome_evento = evento['nome']

    novo_participante = cadastrar_participantes(nome_evento)

    # Verifica duplicidade pelo CPF
    for p in evento['participantes']:
        if p['cpf'] == novo_participante['cpf']:
            print("Participante já cadastrado neste evento!")
            return

    evento['participantes'].append(novo_participante)
    print("Participante cadastrado com sucesso!")