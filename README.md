# Gerenciador de Eventos

Bem-vindo ao meu trabalho final de Algoritmos 1!
Suas principais funcionalidades abrangem o gerenciamento de eventos, permitindo o cadastro, edição e exclusão de eventos; o gerenciamento de participantes, com registro, validação e acompanhamento dos inscritos; e a geração de relatórios e estatísticas, oferecendo análises detalhadas sobre a participação, distribuição etária e popularidade dos eventos. Dessa forma, o sistema facilita a administração completa de eventos, tornando o processo mais ágil, organizado e orientado por dados.
O código foi desenvolvido de forma modular, com cada funcionalidade separada em arquivos específicos, o que facilita manutenções, reaproveitamento de código e futuras expansões, como a implementação de persistência em arquivos, banco de dados ou até mesmo a integração com uma interface gráfica (GUI).

O sistema está dividido em módulos, com responsabilidades específicas:

| Arquivo              | Responsabilidade Principal                                          |
| -------------------- | ------------------------------------------------------------------- |
| `menu.py`            | Estrutura de navegação principal entre menus e funcionalidades.     |
| `evento_registro.py` | Cadastro de eventos, validação de dados, controle de participantes. |
| `participantes.py`   | Cadastro e validações de participantes em eventos existentes.       |
| `listar.py`          | Exibição de eventos e participantes de forma detalhada.             |
| `alterar.py`         | Alteração de dados de eventos                                       |
| `remover.py`         | Exclusão de participantes e eventos                                 |
| `indicadores.py`     | Relatórios quantitativos e análise por geração dos participantes.   |
| `entrada.py`         | Validação de opções do menu                                         |
| `util.py`            | Funções auxiliares (limpar tela)                                         |

Funcionalidades do Projeto

## Cadastro

* Adicionar novos eventos com ID único e endereço completo.
* Inscrever participantes com CPF e data de nascimento válidos.

## Listagem

* Visualizar todos os eventos registrados.
* Ver os detalhes completos de um evento específico.
* Listar todos os participantes de todos os eventos.


## Alteração

* Editar informações dos eventos.

## Remoção

* Remover qualquer participante cadastrado.
* Excluir eventos específicos ou todos os eventos de uma só vez.

## Filtros

* Buscar eventos por mês de realização.
* Filtrar participantes por geração (Baby Boomers, Geração X, Millennials, Geração Z, Alpha).

## Indicadores

* Total de eventos e participantes.
* Evento mais popular.
* Média de participantes por evento.
* Distribuição etária dos inscritos (por geração).

## Gerações Reconhecidas

| Geração       | Idade (em anos) |
| ------------- | --------------- |
| Baby Boomers  | 60 - 78         |
| Geração X     | 44 - 59         |
| Millennials   | 28 - 43         |
| Geração Z     | 12 - 27         |
| Geração Alpha | 0  - 11         |

## Técnicas Aplicadas

* Validação de dados** com `strptime` para datas e regras específicas para CPF e CEP.
* Organização em módulos**, permitindo reutilização de funções e melhor legibilidade.
* Uso de `UUID`** para garantir unicidade dos IDs de eventos e participantes.
* Agrupamento e contagem por geração**, facilitando relatórios demográficos.
* Menus interativos** com tratamento de exceções (`try/except`).


---

Execute o arquivo principal (main.py) para testar o sistema

