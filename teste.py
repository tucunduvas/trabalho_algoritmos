eventos = list()
evento = {
    'id': f"e{1}",
    'nome' : input("Digite o nome do evento: "),
    'data' : input("Data: "),
    'endereço': {
    'rua': input("Rua: "),
    'bairro': input("Bairro: "),
    'cep': input("CEP: ")
    },
}

eventos.append(evento)

nome = evento.get("nome")

print(nome) 

    i = 1 
    for item in eventos:
        i+= 1
        print(f"{i} - {item['nome']}")
    

pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 30},
    {"nome": "Carlos", "idade": 22}
]

# Acessar todos os nomes
for pessoa in pessoas:
    print(pessoa["nome"])

# Acessar apenas o nome da primeira pessoa
print(pessoas[0]["nome"])  # Ana

# Criar uma lista com todos os nomes
nomes = [p["nome"] for p in pessoas]
print(nomes)  # ['Ana', 'Bruno', 'Carlos']


eventos = []
participantes = []

def validar_data():
    # Função simulada para simplificação
    return input("Digite a data do evento (DD/MM/AAAA): ")

def validar_cep():
    # Função simulada para simplificação
    return input("Digite o CEP: ")

def validacao_datanasc():
    # Função simulada para simplificação
    return input("Digite a data de nascimento (DD/MM/AAAA): ")


def cadastrar_participantes(evento_nome):
    qntd = len(participantes)
    participante = {
        'id': f"p{qntd}",
        'nome': input("Digite o nome do participante: "),
        'cpf': input("Digite o cpf do participante: "),
        'data_nasc': validacao_datanasc(),
        'evento_cadastrado': evento_nome
    }
    participantes.append(participante)
    return participante

def cadastrar_evento():
    qntd_evento = len(eventos)
    nome_evento = input("Digite o nome do evento: ")

    evento = {
        'id': f"e{qntd_evento}",
        'nome': nome_evento,
        'data': validar_data(),
        'endereço': {
            'rua': input("Rua: "),
            'bairro': input("Bairro: "),
            'cep': validar_cep()
        },
        'participantes': []
    }

    while True:
        adicionar = input("Deseja adicionar um participante? (s/n): ").lower()
        if adicionar == 's':
            participante = cadastrar_participantes(nome_evento)
            evento['participantes'].append(participante)
        else:
            break

    eventos.append(evento)

# Exemplo de uso:
# cadastrar_evento()
# print(eventos)
# print(participantes)
