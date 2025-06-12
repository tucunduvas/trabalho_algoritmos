from random import randint
import datetime


def cadastrar_participantes(nome_evento, total_participantes):
    participante = {
        'id': f"p{total_participantes}",
        'nome': input("Digite o nome do participante: "),
        'cpf': input("Digite o cpf do participante: "),
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