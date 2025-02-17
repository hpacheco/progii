
# Projeto 4 - Recurso / Melhoria

A próximas tarefas são destinadas a alunos que desejem fazer recurso ou melhora à cadeira. Para estas tarefas vamos utilizar como contexto o campeonato europeu de futebol UEFA Euro 2024.

Aceda aos ficheiros do Projeto 4, onde deve preencher as suas soluções num ficheiro `projeto4.py`:

- Fazendo login no [replit](https://replit.com/) com a conta Google UP (upXXXXX@g.uporto.pt), acendendo à Team [prog2bio2324](https://replit.com/team/prog2bio2324) e iniciando o Projeto4.
- Pode consultar os ficheiros individuais na pasta [projeto4](../scripts/projeto4) e fazer download dos mesmos para desenvolver o projeto no seu computador e utilizando um IDE à sua escolha.
- Pode fazer download de todo o projeto como um arquivo zip [aqui](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2Fhpacheco%2Fprogii%2Ftree%2Fmaster%2Fscripts%2Fprojeto4).
- Se o link anterior não funcionar, pode fazer download de todo o repositório git como um arquivo zip [aqui](https://github.com/hpacheco/progii/archive/refs/heads/master.zip).

## Contexto

Vamos olhar para dois datasets:

* [UEFA-EURO-2024.csv](../scripts/projeto4/dados/UEFA-EURO-2024.csv), que contém uma descrição dos vários jogos calendarizados no torneio, extraído [daqui](https://www.uefa.com/euro2024/standings/);
* [FIFA-Men-Ranking.csv](../scripts/projeto4/dados/FIFA-Men-Ranking.csv), que contém o ranking mundial das várias equipas registadas na FIFA, extraído [daqui](https://inside.fifa.com/fifa-world-ranking/men).


## Tarefa 1 (Árvore do Torneio)

O objetivo desta tarefa é explorar a árvore do torneio de forma a determinar em que fase do torneio é que duas equipas se podem encontrar.

**Complete** a definição da função `dueloEquipas`, que recebe o nome das equipas de países, e returna um tuplo com a fase do torneio (referente à coluna `match_type`) em que as duas equipas se podem encontrar mais cedo no torneio, e uma lista com os estádios (referente à coluna `stadium`) em que podem vir a jogar nessa fase. **Nota:** Pode reparar que duas equipas se encontrarão sempre garantidamente nos quartos de final.

## Tarefa 2 (Fase de Grupos)

O objetivo desta tarefa é visualizar melhor os dados da fase de grupos. Para isso vamos construir um *sunburst chart* - uma generalização de pie charts com vários níveis - utilizando a biblioteca `plotly`. Pode consultar a documentação do `plotly` com exemplos [aqui](https://plotly.com/python/sunburst-charts/).

**Complete** a definição da função `desenhaGrupos`. Desenhar o  gráfico com o `plotly` envolve duas fases:

1. Construir um DataFrame com os dados necessários à visualização. Neste caso, deve criar um DataFrame em que cada linha determina informação de um país, e possui colunas referentes ao nome do país, ao grupo do torneio em que está na fase de grupos, ao seu ranking FIFA e à diferença de pontuação entre o seu ranking atual e o seu ranking anterior. Para isso, deve combinar os dados existentes nos dois datasets fornecidos.
2. Desenhar o DataFrame como um *sunburst chart*, em que o primeiro nível corresponde a cada grupo, e o segundo às equipas dentro desse grupo. Pode encontrar um primeiro esboço de como o fazer no código já fornecido na função `desenhaGrupos`. Para ilustrar melhor cada grupo, pretende-se também que:

    * Defina o tamanho da "fatia" de cada país de forma a que seja tão maior quanto mais elevado for o seu ranking, de forma a exemplificar a dificuldade do grupo.
    * Defina a cor da "fatia" de cada país como sendo proporcional à diferença de pontuação entre o seu ranking atual e anterior, de forma a exemplificar o nível de forma da equipa.

**Nota:** Pode reparar que o `plotly` definirá o tamanho/cor da "fatia" de cada grupo em relação ao somatório dos valores das equipas que constituem o grupo. 
