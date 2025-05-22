
# Projeto 3 - Visualização e animação de dados

Neste terceiro projeto vamos investigar as bibliotecas base de visualização de dados em Python de uma perspetiva prática, e aplicá-las para gerar gráficos e mapas a partir de dados previamente processados.

Aceda aos ficheiros do Projeto 3, onde deve preencher as suas soluções num ficheiro `projeto3.py`:

- Pode consultar os ficheiros individuais na pasta [projeto3](../scripts/projeto3) e fazer download dos mesmos para desenvolver o projeto no seu computador e utilizando um IDE à sua escolha.
- Pode fazer download de todo o projeto como um arquivo zip [aqui](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2Fhpacheco%2Fprogii%2Ftree%2Fmaster%2Fscripts%2Fprojeto3).
- Se o link anterior não funcionar, pode fazer download de todo o repositório git como um arquivo zip [aqui](https://github.com/hpacheco/progii/archive/refs/heads/master.zip).

## Tarefa 1 (Gráficos)

Considere os ficheiros CSV na pasta [codons](../scripts/projeto3/dados/codons), que contêm percentagens do uso de codões para vários organismos. O código dado já está a ler os vários ficheiros para uma estrutura do tipo `dict[str,DataFrame]`. O estudo do uso de codões é frequentemente usado em bioinformática, e muitas vezes visualizado como um mapa de cores.

Utilizando o `matplotlib`, desenhe um mapa de cores de acordo com os seguintes passos:

1. Complete a função `constroiMatrix`, que constrói uma matrix `numpy`, em que linhas são codões e colunas são organismos, e valores percentagem de uso para o par `(codão,organismo)`. 
2. Complete a função `desenhaHeatMap` que desenha um mapa de cores utilizando o `matplotlib`. Para isso deve utilizar a função `imshow` que permite visualizar uma matrix `numpy` como um mapa de cores.

Para obter nota máxima nesta tarefa, o gráfico deve conter alguns extras em termos de formatação, ao critério dos alunos. Como sugestões, podem por exemplo:
* Desenhar labels nos eixos e/ou percentagens por cada célula.
* Acrescentar informação explicativa numa legenda, como um mapa de cores.
* Melhorar espaçamentos do gráfico, já que a proporção de linhas/colunas é bastante acentuada.

## Tarefa 2 (Gráficos Dinâmicos) 

Considere as projeções de população da União Europeia, publicadas [aqui](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Population_projections_in_the_EU#Highlights). Um dos datasets encontra-se disponível localmente no ficheiro [estat_proj_stp24.tsv](../scripts/projeto3/dados/estat_proj_stp24.tsv). Vamos estar  interessados em desenhar um gráfico interativo de projeções de população. Em particular, a primeira coluna do dataset contém `freq,indic_de,projection,geo\TIME_PERIOD`, em que `freq` é a frequência dos dados (sempre `A`, ou seja, anual), `indic_de` é um índice (estamos interessados apenas em `DEATH` para número de mortes, `LBIRTH` para número de nascimentos, `MLEXPEC` para esperança média de vida e `PC_Y15_74` para percentagem de população entre os 15 e 75 anos), `projection` é o valor projetado (estamos apenas interessados em `BSL` significando *baseline*) e `geo\TIME_PERIOD` é o código de um país (encontra também dados para a totalidade dos 27 países).

1. Complete a definição da função `desenhaPopulacaoPaisIndice` que recebe um objeto `Axes` `matplotlib` e o nome de um país, e desenha um gráfico nesse `Axes` com as previsões anuais desse país, para um dado índice.
2. Complete a definição da função `desenhaPopulacao` que cria um gráfico dinâmico de população na UE. Utilize botões interativos `matplotlib` para selecionar quer o país, quer o tipo de índice. Deve desenhar dinamicamente um gráfico para a seleção escolhida.

Note que pode utilizar um comportamento à sua escolha para os botões. Por exemplo, selecionar apenas um ou vários países/índices ao mesmo tempo.

Para obter nota máxima nesta tarefa, o gráfico deve conter alguns extras em termos de formatação, ao critério dos alunos. Como sugestões, podem por exemplo:

* Desenhar cada série num formato diferente, utilizando por exemplo diferentes curvas/barras/áreas, cores, marcadores, etc.
* Conter uma legenda e/ou labels explicativas das séries e dos eixos em questão.
* Visualizar dados agregados de forma diferente, por exemplo juntamente com os dados de cada país.

## Tarefa 3 (Mapas)

Esta tarefa é inspirada no visualizador de dados do portal [invasoras.pt](https://invasoras.pt/) que regista avistamentos de espécies de plantas invasoras em Portugal. Observe os seguintes ficheiros:

* [0008817-250402121839773.csv](../scripts/projeto3/dados/0008817-250402121839773.csv), retirado do portal [GBIF](https://www.gbif.org/pt/dataset/feb41318-374b-4ed6-b61e-0369993abedc) que contém um dataset das ocorrências registadas num período temporal de 7 anos.
* [distritos.geojson](../scripts/projeto3/dados/distritos.geojson), que contém a delimitação geográfica dos vários distritos de Portugal.

Utilizando o `matplotlib` e o `contextily`, desenhe mapas para as seguintes funções:

* Complete a definição da função `desenhaInvasoras`, que desenha um mapa dos vários distritos de Portugal Continental (ignorando as ilhas, para as quais não existem dados significativos neste dataset), com a cor de cada distrito sendo proporcional ao número de espécies invasoras diferentes registadas ao longo do tempo nesse distrito. **Sugestão:** Junte primeiro os dados dos dois ficheiros num só `GeoDataFrame`. 
* Complete a definição da função `desenhaPorto`, que desenha um mapa das ocorrências registadas no distrito do Porto. Cada ocorrência deve ter formato de acordo com a espécie (coluna `species`), cor diferente de acordo com o utilizador que reportou a ocorrência (coluna `identifiedBy`) e tamanho tão maior quanto mais recente for o registo da ocorrência . **Sugestão:** Converta o primeiro ficheiro num `GeoDataFrame`, convertendo as suas colunas que têm coordenadas geográficas apropriadamente.

Para obter nota máxima nesta tarefa, deve aprimorar o desenho dos mapas adequadamente, como por exemplo acrescentando backgrounds, ajustando zoom ou acrescentando labels ou legendas.

## Tarefa 4 (Grafos)

Esta tarefa pretende visualizar uma árvore filogenética utilizada no projeto anterior.
Relembre o ficheiro [21A.json](../scripts/projeto3/dados/21A.json), que contém uma árvore filogenética do vírus SARS-CoV-2, apenas para a variante Delta. A informação deste ficheiro pode ser visualizada na página [SARS-CoV-2 phylogeny](https://nextstrain.org/nextclade/sars-cov-2). O intuito desta tarefa é então replicar parte das capacidades de visualização do portal [nextstrain](https://nextstrain.org). 

Utilizando o `networkx`, desenhe a árvore filogenética de acordo com os seguintes passos:

1. Complete a definição da função `constroiGrafo` que retorna um grafo direcionado correspondente, em que cada variante é um nodo e arestas definem mutações da variante A para a variante B. Anote o grafo com informação adicional útil para a visualização, em particular ao nível de cada nodo (um atributo `clade` com o identificador Clade, campo `node_attrs.clade_nextstrain.value` no formato original) e de cada aresta (um atributo `div` com a diferença de divergência da variante B em relação à variante A, campo `node_attrs.div` no formato original).
2. Complete a definição da função `desenhaFilogenetica`, que desenha o grafo construído pela função anterior. Configure a formatação a seu gosto, respeitando a seguintes indicações:

    * O layout deve refletir a estrutura hierárquica da árvore filogenética.
    * O desenho de cada nodo deve utilizar os atributos, em particular o seu identificador Clade. Podem não representar os identificadores de todos os nodos para aliviar a visualização. Podem também associar identificadores Clade a um mapa de cores, como é feito pelo nextstrain.
    * O desenho de cada aresta (cor, espessura, etc) deve refletir a divergência entre as duas variantes.





