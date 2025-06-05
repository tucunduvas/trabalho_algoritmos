from random import randint
import datetime

import evento

participantes = list()
qntd = len(participantes)

def cadastrar_participantes():
    participante = {
        'id': f"p{qntd}",
        'nome': input("Digite o nome do participante: "),
        'cpf': input("Digite o cpf do participante: "),
        'data_nasc': validacao_datanasc(),
        'evento_cadastrado': evento.get('nome'), #quero buscar em quais eventos o participante esta cadastrado 
    }
    
def validacao_datanasc():
    try: 
        data_nascimento = int(input(datetime.date("Digite a data de nascimento do participante, no formato dia/mes/ano e com apenas números: ")))
        if len(data_nascimento)==8:
            return data_nascimento
    except ValueError:
        pass
    print("Inválido! O campo data de nascimento aceita apenas numeros no formato dia/mês/ano, tente novamente!")
    return -1