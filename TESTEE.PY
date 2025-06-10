pessoas = [
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