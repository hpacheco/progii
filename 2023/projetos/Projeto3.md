
# Projeto 3 - Visualização e animação de dados

Neste terceiro projeto vamos investigar as bibliotecas base de visualização de dados em Python de uma perspetiva prática, e aplicá-las para gerar gráficos e mapas a partir de dados previamente processados.

Aceda aos ficheiros do Projeto 3, onde deve preencher as suas soluções num ficheiro `projeto3.py`:

- Fazendo login no [replit](https://replit.com/) com a conta Google UP (upXXXXX@g.uporto.pt), acendendo à Team [prog2bio2223](https://replit.com/team/prog2bio2223) e iniciando o Projeto3.
- Pode consultar os ficheiros individuais na pasta [projeto3](../scripts/projeto3) e fazer download dos mesmos para desenvolver o projeto no seu computador e utilizando um IDE à sua escolha.
- Pode fazer download de todo o projeto como um arquivo zip [aqui](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/hpacheco/progii/tree/master/scripts/projeto3).

## Tarefa 1 (Gráficos)

Vamos considerar um dataset clássico em bioinformática sobre dados de diagnóstico de cancro da mama por paciente, retirado [desta](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)) fonte e disponibilizado como um ficheiro CSV [aqui](../scripts/projeto3/dados/breast_cancer.csv). Pode encontrar uma descrição detalhada das colunas [aqui](https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.names).

**Complete** a função `desenhaDiagnostico` que desenha um gráfico, no formato *scatter plot*, que evidencie a correlação entre alguns atributos e o diagnóstico final. Mais concretamente, desenhe um gráfico com os atributos `Uniformity of Cell Size` e Uniformity of `Cell Shape` nos eixos dos XX e YY, respetivamente. Desenhe cada ponto com uma cor indicativa do seu diagnóstico (atributo `Class`).

Para obter nota máxima nesta tarefa, o gráfico deve conter alguns extras como, por exemplo:

* uma vez que podem existir várias entradas para o mesmo par de valores XY, desenhe o tamanho de cada ponto proporcionalmente ao número de entradas;
* aumente a dimensionalidade do gráfico desenhando atributos adicionais como margens de erro ou estilos diferentes; (**NOTA:** Pode investigar quais os atributos mais correlacionados calculando o método `.corr()` do DataFrame.)
* acrescente informação explicativa na label de cada eixo e/ou numa legenda.

## Tarefa 2 (Gráficos Dinâmicos) 

Considere o dataset de estimativa à data de 2023 de stocks de armas nucleares, publicado [aqui](https://fas.org/issues/nuclear-weapons/status-world-nuclear-forces/) e disponível localmente no ficheiro [nuclear_forces.csv](../scripts/projeto3/dados/nuclear_forces.csv).

1. **Complete** a definição da função `desenhaNuclearPais` que recebe um objeto `Axes` matplotlib e o nome de um país, e desenha um gráfico `pie` nesse `Axes` com a distribuição de stocks de armas nucleares por categoria para esse país. Cada fatia da tarte deve mencionar o número total ou percentagem de armas em questão.
2. **Complete** a definição da função `desenhaNuclearCategoria` que recebe um objeto `Axes` matplotlib e o nome de uma categoria, e desenha um gráfico `pie` nesse `Axes` com a distribuição de stocks de armas nucleares por país para essa categoria. Cada fatia da tarte deve mencionar o número total ou percentagem de armas em questão.
3. **Complete** a definição da função `desenhaNuclear` que cria um gráfico dinâmico de stocks de armas nucleares. Utilize dois `RadioButtons` (um com uma listagem de países e outro com listagem de categorias) para selecionar qualquer seleção de país ou categoria. Deve desenhar dinamicamente um gráfico `pie` para a seleção escolhida. Tanto países como categorias devem incluir uma opção `Todos`; desenhe o gráfico que achar mais adequado para apresentar toda a informação quando ambas as opções `Todos` estão selecionadas.

## Tarefa 3 (Mapas) (Valorização)

Esta tarefa é inspirada [neste](https://www.emcdda.europa.eu/publications/html/pods/waste-water-analysis_en#data-explorer) visualizador de dados da União Europeia sobre deteção de drogas em análises de águas residuais.

Observe os seguintes ficheiros:

* [wastewaterData.csv](../scripts/projeto3/dados/wastewaterData.csv), que contém medições (agregadas por dia da semana) de vários metabólitos em várias cidades Europeias entre 2011 e 2022.
* [wastewaterSites.csv](../scripts/projeto3/dados/wastewaterSites.csv), que contém a geolocalização das estações de tratamento de águas utilizadas no estudo. 

Utilizando o `matplotlib` e o `contextily`, desenhe um mapa interativo que mostre os dados por metabólito e por ano. Siga os seguintes passos:

1. **Complete** a definição da função `leWasteGeo` que lê os ficheiros CSV acima e retorna um `GeoDataFrame` que combina a informação de ambos.
2. **Complete** a definição da função `desenhaMetabolitoAno`, que recebe um tuplo `(ax,gdf,metabolito,ano)` e desenha no `Axes` `ax` um mapa com as análises desse `metabolito` nesse `ano` encontradas no `GeoDataFrame` `gdf`. Para cada registo, deve desenhar um marcador na geolocalização correspondente com tamanho proporcional à média diária registada.
3. **Complete** a definição da função `desenhaMapa` que cria o mapa interativo, e chama as funções definidas antes. Pode e deve ajustar a função `desenhaMetabolitoAno` de forma a que as visualizações de várias combinações de metabólito e ano sejam consistentes.

## Tarefa 4 (Grafos)

Esta tarefa pretende visualizar relações entre alguns genes sequenciados a partir do genoma de ratos. Considere o ficheiro [genes.txt](../scripts/projeto3/dados/genes.txt) retirado do site [Mouse Genome Informatics](https://www.informatics.jax.org/).
Em particular, vamos querer realçar características comuns, classificadas de acordo com o seu *Mammalian Phenotype*, entre genes de cromossomas diferentes.
Utilizando o `networkx`, desenhe um mapa circular de acordo com os seguintes passos:

0. Inspecione o `DataFrame` `genes` que prepara a informação relevante dos genes.
1. **Complete** a definição da função `identificaGenes`, que recebe uma string com um subtermo a salientar (por exemplo, 'brain' ou 'renal'), e retorna um grafo em que os nodos são todos os genes, colocando o campo `Chr` como atributo de cada nodo. Se dois genes partilharem o mesmo termo ~~subtermo~~ (i.e., se o ~~subtermo for uma substring do~~ campo `Term` ~~de cada um~~ dos genes for igual), então deve acrescentar uma aresta entre esses nodos com o campo `Term` como atributo. **NOTA:** é importante que a ordem dos nodos no grafo (como visível na lista `grafo.nodes()`) seja a mesma que a ordem dos genes no `DataFrame` `genes`.
2. **Complete** a definição da função `desenhaGenes`, que desenha o grafo construído pela função `identificaGenes` utilizando o `nx.circular_layout`. Defina a cor de cada nodo/gene de acordo com o cromossoma a que pertence; cada gene deve aparecer desenhado ao lado dos outros genes que partilham o cromossoma. Configure a restante formatação (labels, cores, tamanhos, etc) a seu gosto.

## Tarefa 5 (Web) (Valorização)

Esta tarefa pretende desenhar uma animação web da evolução das temperaturas mínima e máxima em Portugal ao longo dos últimos 90 anos, disponibilizadas pelo [IPMA](www.ipma.pt/en/oclima/series.longas/).
Utilizando o `pandas` e o `plotly`, desenhe a animação de acordo com os seguintes passos:

0. Inspecione o dicionário de `DataFrame`s `dfs` que contém a informação relevante.
1. **Complete** a definição da função `analizaTemperaturas`, que retorna um só `DataFrame` com os dados no formato necessário para gerar a animação. Em particular, o `DataFrame` resultante deve ter as seguintes colunas: `year` (ano entre `1931` e `2019`), `season` (`Spring`,`Summer`,`Autumn` ou `Winter`), `type` (`tmin` ou `tmax`), `cum` (`False` se o mínimo/máximo desse ano ou `True` se o mínimo/máximo acumulado até esse ano) e `temp` (valor da temperatura) **Sugestão:** utilize os métodos `cummax`, `cummin` e `melt` do `pandas`.
2. **Complete** a definição da função `desenhaTemperaturas` que gera um ficheiro HTML com a animação da evolução das temperaturas ao longo dos anos. Desenhe um scatter plot com a evolução anual das várias temperaturas. Pode ajustar cores, símbolos, labels ou legendas a gosto.




