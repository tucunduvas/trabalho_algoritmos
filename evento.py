import datetime
from participantes import cadastrar_participantes
eventos = list()
qntd_evento = len(eventos)
def cadastrar_evento():
    evento = {
        'id': f"e{qntd_evento}",
        'nome' : input("Digite o nome do evento: "),
        'data' : int(input(datetime.date("Digite a data do evento, seguindo a estrutura dia/mês/ano em números: "))), #try catch aqui 
        'endereço': {
            'rua': input("Rua: "),
            'bairro': input("Bairro: "),
            'cep': input("CEP: ")
        },
        'participantes': cadastrar_participantes()
    }
    
