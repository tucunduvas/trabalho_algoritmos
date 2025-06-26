
alunos = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 30},
    {"nome": "Carlos", "idade": 22}
]

valores = list()
for i in alunos:
    valores.append(i.values())
    
    
for i,j in enumerate(valores):
    print(f"{i} - {j}")

def remover(opcao):
    del alunos[opcao]
    print(alunos)
opcao = int(input("Digite qual aluno deseja remover: "))
remover(opcao)
    