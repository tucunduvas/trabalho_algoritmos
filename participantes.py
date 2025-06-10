from random import randint
import datetime
from eventoos import cadastrar_evento
from eventoos import qntd

def cadastrar_participantes(nome_evento):
    participante = {
        'id': f"p{qntd}",
        'nome': input("Digite o nome do participante: "),
        'cpf': input("Digite o cpf do participante: "),
        'data_nasc': validacao_datanasc(),
        'evento_cadastrado': nome_evento
    }
    return participante

def validacao_datanasc():
    try: 
        data_nascimento = int(input(datetime.date("Digite a data de nascimento do participante, no formato dia/mes/ano e com apenas números: ")))
        if len(data_nascimento)==8:
            return data_nascimento
    except ValueError:
        pass
    print("Inválido! O campo data de nascimento aceita apenas numeros no formato dia/mês/ano, tente novamente!")
    return -1