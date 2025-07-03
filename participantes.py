from random import randint
import datetime
import uuid


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
        pass
    print("Inválido! O campo data de nascimento aceita apenas numeros no formato dia/mês/ano, tente novamente!")
    return -1


def validacao_cpf():
    cpf = input(("Digite  o cpf do participante, com apenas números: "))
    try: 
        if len(cpf)==11:
            return cpf
    except ValueError:
        pass
    print("Inválido! O campo cpf aceita apenas números, tente novamente!")
    return -1