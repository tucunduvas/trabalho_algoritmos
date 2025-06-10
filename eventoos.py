import datetime
from participantes import cadastrar_participantes
eventos = list()

def cadastrar_evento():
    qntd_evento = len(eventos)
    nome_evento = input("Digite o nome do evento: ")
    evento = {
        'id': f"e{qntd_evento}",
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
    try:
        data = int(input(datetime.date("Digite a data do evento, seguindo a estrutura dia/mês/ano em números: ")))
        if len(data)==8: 
            return data
    except ValueError:
        pass
    print("Inválido! O campo data aceita apenas numeros no formato dia/mês/ano, tente novamente!")
    return -1

def validar_cep():
    try:
        cep = int(input(("Digite o CEP, ultilizando apenas números: ")))
        if len(cep)==8: 
            return cep
    except ValueError:
        pass
    print("Inválido! O campo CEP aceita apenas números, tente novamente!")
    return -1


