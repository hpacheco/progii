
# Projeto 4 - Recurso / Melhoria

A próximas tarefas são destinadas a alunos que desejem fazer recurso ou melhora à cadeira. Para estas tarefas vamos utilizar como contexto o campeonato mundial de Formula 1, ou simplesmente F1.

Uma das principais características da F1 é a grande quantidade de dados dos carros em tempo real e a sua análise para maximizar performance. A biblioteca [FastF1](https://theoehrly.github.io/Fast-F1/) fornece uma grande quantidade de dados recolhidos ao longo de cada corrida. 

Aceda aos ficheiros do Projeto 4, onde deve preencher as suas soluções num ficheiro `projeto4.py`:

- Fazendo login no [replit](https://replit.com/) com a conta Google UP (upXXXXX@g.uporto.pt), acendendo à Team [prog2bio2223](https://replit.com/team/prog2bio2223) e iniciando o Projeto4.
- Pode consultar os ficheiros individuais na pasta [projeto4](../scripts/projeto4) e fazer download dos mesmos para desenvolver o projeto no seu computador e utilizando um IDE à sua escolha.
- Pode fazer download de todo o projeto como um arquivo zip [aqui](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/hpacheco/progii/tree/master/scripts/projeto4).

## Tarefa 1 (Qualificação intra-equipa)

No campeonato de F1, cada evento tem uma fase de qualificação e uma corrida.
Uma das estatísticas mais recorrentes na F1 são os duelos de qualificação entre os dois pilotos de cada equipa. 
Para cada evento, um piloto ganha o duelo se ficar melhor colocado na qualificação: atingindo uma fase de qualificação mais avançada e/ou fazendo um menor tempo. [^1]

[^1]: Existem 3 fases de qualificação (começando na Q1 e acabando na Q3). Na Q1 e Q2 os pilotos com os 5 piores tempos são eliminados; a Q3 determina a seriação dos 10 melhores pilotos.

No ficheiro `projeto4.py` pode encontrar duas funções pré-definidas que recolhem informações relevantes:
* `getSchedule` retorna uma sequência com todos os eventos num campeonato, identificado pelo ano;
* `getQualifyingLapTimes` retorna informação sobre a qualificação de um dado evento organizado por equipas (10), pilotos (2 por equipa, os indivíduos podem excepcionalmente variar) e fases de qualificação (3), organizada como um dicionário de dicionários com a seguinte forma:

```python
{team1:
    {driver1:
        {'Q1': Timedelta(...), 'Q2': Timedelta(...)}
    ,driver2:
        {'Q1': Timedelta(...), 'Q2': Timedelta(...), 'Q3': Timedelta(...)
    }
...
}
```

**Complete** a função `teamDuels`, que retorna os duelos por equipa durante um campeonato. O resultado deve ser um dicionário de dicionários com a seguinte forma:

```python
{team1: {driver1: 15, driver2: 7}, ... } 
```

O ficheiro [main.py](../scripts/projeto4/main.py) contém alguns testes que deve utilizar para verificar a correção da sua solução.

**Nota:** Pode ser útil definir uma função auxiliar que calcula o resultado de um duelo para um evento, e combinar essa função para calcular o resultado agregado dos duelos para todos os eventos do campeonato.

## Tarefa 2 (Melhores voltas de qualificação)

Outra informação que podemos obter é a telemetria (posição, velocidade, distância percorrida, etc) de cada carro em tempo real ao longo do seu percurso.
A função `getQualifyingFastestLaps` retorna informação de telemetria (um `DataFrame` ordenado por tempo) da melhor volta de qualificação de cada piloto, com o seguinte formato:

```python
{ driver1 : {'TeamName': team1, 'TeamAbbreviation': abr1, 'TeamColor': color1, 'Telemetry': DataFrame(...), ... }
```

O objetivo desta tarefa é construir uma animação das melhores voltas de qualificação para um dado evento. Para isso, iremos gerar um gráfico de barras horizontais utilizando `plotly`, colocando:

* no eixo dos X a distância percorrida;
* no eixo dos Y uma barra referente a cada piloto;
* na dimensão temporal os segundos decorridos, como um inteiro (uma sequência de números inteiros `0,1,2,...` até ao tempo máximo da animação)
* uma legenda com a equipa de cada piloto, em que a barra de cada piloto deve ter a cor da sua equipa.

Para isso, deve gerar um `DataFrame` que contenha cada campo relevante para a animação como uma coluna independente.

**NOTA:** É essencial normalizar os dados de telemetria de cada piloto para a mesma escala temporal. Considere utilizar os métodos `reindex` e `ffill` do `pandas`.

**Complete** a função `drawFastestLaps` que constrói a animação como um ficheiro HTML. Por exemplo, para a invocação `drawFastestLaps(2021,'Austrian Grand Prix')`, o resultado final deve ser uma animação similar à seguinte:

<iframe
  src="quali.html"
  style="width:100%; height:300px;"
></iframe>


