from evento_registro import eventos
from util import limpar_tela
from saida import sair
from datetime import datetime

def calcular_idade(data_nasc):
    dia, mes, ano = map(int, data_nasc.split("/"))
    hoje = datetime.today()
    return hoje.year - ano - ((hoje.month, hoje.day) < (mes, dia))

def classificar_geracao(idade):
    if 60 <= idade <= 78:
        return "Baby Boomers"
    elif 44 <= idade <= 59:
        return "Geração X"
    elif 28 <= idade <= 43:
        return "Millennials"
    elif 12 <= idade <= 27:
        return "Geração Z"
    else:
        return "Geração Alpha"

def mostrar_indicadores():
    limpar_tela()
    
    total_eventos = len(eventos)
    total_participantes = 0
    participantes_por_evento = {}
    geracoes = {
        "Baby Boomers": 0,
        "Geração X": 0,
        "Millennials": 0,
        "Geração Z": 0,
        "Geração Alpha": 0
    }

    for evento in eventos:
        participantes = evento.get('participantes', [])
        total_participantes += len(participantes)
        participantes_por_evento[evento['nome']] = len(participantes)

        for participante in participantes:
            idade = calcular_idade(participante['data_nasc'])
            geracao = classificar_geracao(idade)
            geracoes[geracao] += 1

    evento_mais_popular = max(participantes_por_evento, key=participantes_por_evento.get, default="Nenhum")
    media_participantes = total_participantes / total_eventos if total_eventos > 0 else 0

    print("______INDICADORES______")
    print(f"Total de eventos cadastrados: {total_eventos}")
    print(f"Total de participantes: {total_participantes}")
    print(f"Evento com mais participantes: {evento_mais_popular} ({participantes_por_evento.get(evento_mais_popular, 0)} participantes)")
    print(f"Média de participantes por evento: {media_participantes:.2f}")
    print("Participantes por geração:")
    for geracao, quantidade in geracoes.items():
        print(f"  {geracao}: {quantidade}")
    
    input("Aperte a tecla Enter para voltar.")
