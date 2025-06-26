from operator import add


alunos = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 30},
    {"nome": "Carlos", "idade": 22}
]
pessoas= [
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 30},
    {"nome": "Carlos", "idade": 22}
]
eventos= [
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 30},
    {"nome": "Carlos", "idade": 22}
]

# Acessar todos os nomes
for pessoa in pessoas:
    print(pessoa["nome"])
    
i = 1 
for item in pessoas:
    i+= 1
    print(f"{i} - {item['nome']}")
    
la = {'oi': 1, 'tchau': 2}

la.update

nomes_evento = list(eventos.keys())
for i, j in enumerate(nomes_evento):
    print(f"{i} - {j}")
    opcao = ler_opcao(len(nomes_evento)-1)
    
for e in eventos:
    if 



from entrada import ler_opcao  
opcao = 1
if opcao==1:
    print("de qual aluno deseja adicionar: ")
    nomes = list(alunos.keys())
    for i,j in enumerate(nomes):
        print(f"{i} - {j}")
        opcao = ler_opcao(len(nomes)-1)
        nome = nomes[opcao]
        add(nome)
        if opcao==2:
            break