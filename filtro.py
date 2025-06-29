
from datetime import datetime
from evento_registro import eventos

def filtro_tema():
    pass

def filtro_mes():
    pass

def filtro_qntd_participantes():
    pass

#geracoes

todos_participantes = []
for evento in eventos:
    todos_participantes.extend(evento['participantes'])

def genz(participante):
    data_nasc = datetime.strptime(participante['data_nasc'], "%d/%m/%Y")
    return 2012>=data_nasc.year >= 1997


participantes_genz = list(filter(genz, todos_participantes))

for _ in participantes_genz:
    print(_['nome'])
    
    
def genx(participante):
    data_nasc = datetime.strptime(participante['data_nasc'], "%d/%m/%Y")
    return 1965<=data_nasc.year<=1980


participantes_genx = list(filter(genx, todos_participantes))

for _ in participantes_genx:
    print(_['nome'])
    
def millenials(participante):
    data_nasc = datetime.strptime(participante['data_nasc'], "%d/%m/%Y")
    return 1981<=data_nasc.year<=1996


participantes_millenials = list(filter(millenials, todos_participantes))

for _ in participantes_millenials:
    print(_['nome'])
    
    
def babyboomers(participante):
    data_nasc = datetime.strptime(participante['data_nasc'], "%d/%m/%Y")
    return 1946<=data_nasc.year<=1964


participantes_babyboomers = list(filter(babyboomers, todos_participantes))

for _ in participantes_babyboomers:
    print(_['nome'])
    

