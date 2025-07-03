import datetime
from participantes import cadastrar_participantes
import uuid

import uuid

eventos = [
    {
        'id': f"e{uuid.uuid4()}",
        'nome': "Congresso de Tecnologia",
        'data': "15/09/2025",
        'endereço': {
            'rua': "Rua das Inovações",
            'bairro': "Centro Tech",
            'cep': "12345-000"
        },
        'participantes': [
            {
                'id': f"p{uuid.uuid4()}",
                'nome': "Alice Souza",
                'cpf': "111.111.111-11",
                'data_nasc': "01/01/1990",
                'evento_cadastrado': "Congresso de Tecnologia"
            },
            {
                'id': f"p{uuid.uuid4()}",
                'nome': "Bruno Lima",
                'cpf': "222.222.222-22",
                'data_nasc': "12/05/1985",
                'evento_cadastrado': "Congresso de Tecnologia"
            }
        ]
    },
    {
        'id': f"e{uuid.uuid4()}",
        'nome': "Feira de Startups",
        'data': "20/10/2025",
        'endereço': {
            'rua': "Avenida Empreendedora",
            'bairro': "Inova Bairro",
            'cep': "54321-000"
        },
        'participantes': [
            {
                'id': f"p{uuid.uuid4()}",
                'nome': "Carla Mendes",
                'cpf': "333.333.333-33",
                'data_nasc': "10/09/1992",
                'evento_cadastrado': "Feira de Startups"
            },
            {
                'id': f"p{uuid.uuid4()}",
                'nome': "Ygor Guilherme",
                'cpf': "377.345.990-33",
                'data_nasc': "10/05/2006",
                'evento_cadastrado': "Feira de Startups"
            },
            {
                'id': f"p{uuid.uuid4()}",
                'nome': "Daniel Rocha",
                'cpf': "444.444.444-44",
                'data_nasc': "22/03/1988",
                'evento_cadastrado': "Feira de Startups"
            }
        ]
    },
    {
        'id': f"e{uuid.uuid4()}",
        'nome': "Encontro de Devs",
        'data': "05/11/2025",
        'endereço': {
            'rua': "Rua do Código",
            'bairro': "Bairro Dev",
            'cep': "67890-000"
        },
        'participantes': [
            {
                'id': f"p{uuid.uuid4()}",
                'nome': "Eduardo Tavares",
                'cpf': "555.555.555-55",
                'data_nasc': "07/07/1995",
                'evento_cadastrado': "Encontro de Devs"
            },
            {
                'id': f"p{uuid.uuid4()}",
                'nome': "Fernanda Silva",
                'cpf': "666.666.666-66",
                'data_nasc': "30/11/1993",
                'evento_cadastrado': "Encontro de Devs"
            }
        ]
    }
]


# uuid
def cadastrar_evento():
    qntd_evento = len(eventos)
    nome_evento = input("Digite o nome do evento: ")
    evento = {
        'id': f"e{uuid.uuid4()}",
        'nome' : nome_evento,
        'data' : validar_data(),
        'endereço': {
            'rua': input("Rua: "),
            'bairro': input("Bairro: "),
            'cep': validar_cep()
        },
        'participantes': []
    }
    qntd = evento.get(len('participante'))
    while True:
        adicionar = input("Deseja adicionar um participante? (s/n): ").lower()
        if adicionar == 's':
            participante = cadastrar_participantes(nome_evento)
            evento['participantes'].append(participante)
        else:
            break
    eventos.append(evento)
    
def validar_data():
    while True:
        data = input("Digite a data do evento, seguindo a estrutura dia/mês/ano: ")
        try:
            datetime.datetime.strptime(data,'%d/%m/%Y')
            return data
        except ValueError:
            print("Inválido! O campo data aceita apenas numeros no formato dia mês ano, tente novamente!")


def validar_cep():
    while True:
        cep = input(("Digite o CEP, ultilizando apenas números: "))
        try:
            if len(cep)==8 and cep.isdigit(): 
                return cep
        except ValueError:
            print("Inválido! O campo CEP aceita apenas números, tente novamente!")


