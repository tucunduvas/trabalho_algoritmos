import datetime
from participantes import cadastrar_participantes
eventos = list()
qntd_evento = len(eventos)
def cadastrar_evento():
    evento = {
        'id': f"e{qntd_evento}",
        'nome' : input("Digite o nome do evento: "),
        'data' : validar_data(),
        'endereço': {
            'rua': input("Rua: "),
            'bairro': input("Bairro: "),
            'cep': input("CEP: ")
        },
        'participantes': cadastrar_participantes()
    }
    
def validar_data():
    try:
        data = int(input(datetime.date("Digite a data do evento, seguindo a estrutura dia/mês/ano em números: ")))
        if len(data)==8: 
            return data
    except ValueError:
        pass
    print("Inválido! O campo data aceita apenas numeros no formato dia/mês/ano, tente novamente!")
    return -1
