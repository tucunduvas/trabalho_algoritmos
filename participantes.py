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
        'data_nasc': int(input(datetime.date("Digite a data de nascimento do participante, no formato dia/mes/ano e com apenas números: "))), #por try catch ou except aqui
        'evento_cadastrado': evento.get('nome'), #quero buscar em quais eventos o participante esta cadastrado 
    }