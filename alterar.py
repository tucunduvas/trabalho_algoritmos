from evento_registro import eventos
from util import limpar_tela
from entrada import ler_opcao
from saida import sair 
from evento_registro import validar_data
from evento_registro import validar_cep

def alterar_evento():
    limpar_tela()
    while True:
        print("___Qual evento deseja alterar?___")
        print("1 - Voltar")
        print("2 - Sair")
        i = 2
        for i,item in enumerate(eventos, start=3):
            print(f"{i} - {item['nome']}")
        opcao = ler_opcao(len(eventos)+2)
        
        opcoes = { 
            1: None,
            2: sair,
            }
        
        if opcao == 2:
            break
        
        if opcao >= 3 and opcao < len(eventos) + 3:
            deseja_alterar(eventos[opcao - 3])

            
        if opcoes.get(opcao):
                opcoes[opcao]()


def deseja_alterar(evento):
    while True:
        print("Deseja alterar o que? ")
        print("1 - Sair")
        print("2 - Voltar")
        print(f"3 - Nome: {evento['nome']}")
        print(f"4 - Data: {evento['data']}")
        endereco = evento.get('endereço')
        if endereco:
            print(f"5 - Rua: {endereco.get('rua')}")
            print(f"6 - Bairro: {endereco.get('bairro')}")
            print(f"7 - CEP: {endereco.get('cep')}")
            opcao = ler_opcao(7)
        
        opcoes = {
            2: None,
            1: sair,
            3: alterar_nome,
            4: alterar_data,
            5: alterar_rua,
            6: alterar_bairro,
            7: alterar_cep,
        }
        
        if opcoes.get(opcao):
            opcoes[opcao](evento)
            
            
def alterar_nome(evento):
    
    evento.update({'nome': input("Digite o nome:")})
    print("Alteração realizada com sucesso.")
    
    print("1 - Sair")
    print("2 - Voltar")
    opcao = ler_opcao(2)
    opcoes = {
        1 : sair,
        2: None,
    }
    if opcoes.get(opcao):
        opcoes[opcao](evento)
    
def alterar_data(evento):
    limpar_tela()
    evento.update({'data': validar_data()})
    print("Alteração realizada com sucesso.")
    
    print("1 - Sair")
    print("2 - Voltar")
    opcao = ler_opcao(2)
    opcoes = {
        1 : sair,
        2: None,
    }
    if opcoes.get(opcao):
        opcoes[opcao](evento)
        
def alterar_rua(evento):
    limpar_tela()
    endereco = evento.get('endereço')
    endereco.update({'rua': input("Digite a rua: ") })
    print("Alteração realizada com sucesso.")
    
    print("1 - Sair")
    print("2 - Voltar")
    opcao = ler_opcao(2)
    opcoes = {
        1 : sair,
        2: None,
    }
    if opcoes.get(opcao):
        opcoes[opcao](evento)
        
def alterar_bairro(evento):
    limpar_tela()
    endereco = evento.get('endereço')
    endereco.update({'bairro': input("Digite o bairro: ") })
    print("Alteração realizada com sucesso.")
    print("1 - Sair")
    print("2 - Voltar")
    opcao = ler_opcao(2)
    opcoes = {
        1 : sair,
        2: None,
    }
    if opcoes.get(opcao):
        opcoes[opcao](evento)
    
def alterar_cep(evento):
    limpar_tela()
    evento['endereco'].update({'cep': validar_cep()}) 
    print("Alteração realizada com sucesso.")
    print("1 - Sair")
    print("2 - Voltar")
    opcao = ler_opcao(2)
    opcoes = {
        1 : sair,
        2: None,
    }
    if opcoes.get(opcao):
        opcoes[opcao](evento)
