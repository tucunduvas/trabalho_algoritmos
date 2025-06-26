
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
    opcao = input("Digite qual aluno deseja remover: ")
    

for i in valores:
    if i == 'Ana':
        alunos.remove(opcao)
        
        
print(alunos)