
# Projeto 3 - Visualização e animação de dados

Neste terceiro projeto vamos investigar as bibliotecas base de visualização de dados em Python de uma perspetiva prática, e aplicá-las para gerar gráficos e mapas a partir de dados previamente processados.

Aceda ao repositório [replit](https://replit.com/@up652136/Prog2-Proj3) do Projeto 3, onde pode encontrar um ficheiro `projeto3.py`:

- Criando uma conta no [replit](https://replit.com/) e fazendo `Fork` do projeto, pode resolver o projeto online utilizando o IDE web. 
- Pode consultar os ficheiros individuais na pasta [projeto3](../scripts/projeto3) e fazer download dos mesmos para desenvolver o projeto no seu computador e utilizando um IDE à sua escolha.
- Pode fazer download de todo o projeto como um arquivo zip [aqui](../scripts/projeto3.zip).

## Tarefa 1 (Gráficos)

Observe os seguintes ficheiros CSV:

* [brent.csv](../scripts/projeto3/dados/brent.csv), retirado [daqui](https://www.macrotrends.net/2480/brent-crude-oil-prices-10-year-daily-chart), que contém a evolução do preço em Dólares por Barril de Brent nos mercados internacionais;
* [gasolina.csv](../scripts/projeto3/dados/gasolina.csv), retirado [daqui](https://precoscombustiveis.dgeg.gov.pt/estatistica/preco-medio-diario/), que contém a evolução do preço em Euros por Litro de Gasolina Simples 95 em Portugal, desde 2015.

**Complete** a função `desenhaPrecos` que desenha um gráfico que demonstre a forte correlação entre os preços do barril de Brent e da Gasolina Simples 95, desde 2019.
Para obter nota máxima nesta tarefa, o gráfico deve:

* desenhar cada curva com um estilo (linhas, marcadores, cores, áreas, barras, etc) diferente;
* conter informação explicativa na label de cada eixo e/ou numa legenda;
* desenhar cada curva num eixo dos Y independente;
* marcar com anotações dois momentos relevantes: o início da pandemia de COVID-19 e o início da guerra na Ucrânia.

## Tarefa 2 (Gráficos Dinâmicos) 

Observe os ficheiros CSV contidos na pasta [ukraine-refugees](../scripts/projeto3/dados/ukraine-refugees), obtidos [aqui](https://github.com/datadesk/ukraine-refugee-tracker/tree/main/raw/daily), que contêm dados de refugiados ucranianos durante o conflito atual para diversos países europeus.

1. **Complete** a definição da função `desenhaRefugiadosDia` que recebe um objecto `Axes` matplotlib e um dia `YYYY-mm-dd` e desenha um gráfico *pie* nesse `Axes` com os números de refugiados Ucranianos para os diferentes países nesse dia. Cada fatia da tarte deve mencionar o país em questão e o número de refugiados.
2. **Complete** a definição da função `desenhaRefugiadosDias` que cria um gráfico dinâmico para os vários dias de conflito disponíveis. Utilize um `Slider` matplotlib para controlar o dia e evite erros quando houver dias em falta.

## Tarefa 3 (Mapas) (Valorização)

Esta tarefa é inspirada [neste](https://data.humdata.org/visualization/ukraine-humanitarian-operations/) visualizador de dados sobre o conflito atual na Ucrânia.

Observe os seguintes ficheiros:

* [Ukraine-regions.geojson](../scripts/projeto3/dados/Ukraine-regions.geojson), retirado [daqui](https://raw.githubusercontent.com/org-scn-design-studio-community/sdkcommunitymaps/master/geojson/Europe/Ukraine-regions.json), que contém informação sobre os contornos geográficos de cada uma das regiões da Ucrânia. Pode visualizar as regiões num mapa online carregando o ficheiro em <https://geojson.io/>.
* [ukraine-population.csv](../scripts/projeto3/dados/ukraine-population.csv), adaptado [daqui](http://database.ukrcensus.gov.ua/PXWEB2007/eng/news/op_popul_e.asp), que contém a população da Ucrânia por região no início do ano de 2022. 

Utilizando o `Folium`, desenhe um mapa *chloropeth* das regiões da Ucrânia, em que a cor de cada região é proporcional à densidade populacional de cada região (pessoas / km2). Siga os seguintes passos:

1. **Complete** a definição da função `populacaoUcrania` que combina ambos os ficheiros num só `GeoDataFrame`. Notas:

    - A função deve retornar um novo `GeoDataFrame` com duas novas colunas `regiao` (nome de cada região) e `densidade` (densidade populacional de cada região).
    - Considere uma densidade por defeito (por exemplo 0) para regiões sem informação de população.
    - Ajuste manualmente a densidade da cidade de Kiev, que é muito maior, para evitar que "ofusque" todas as outras densidades.
    - A área de cada região já se encontra disponível no ficheiro GeoJSON com dados de regiões.
    - Os nomes de regiões em ambos os datasets não são iguais. Deve fazer o mapeamento manualmente.

2. Consulte a função a função `desenhaPopulacaoUcrania` que desenha o mapa *cloropeth*. Adapte a seu gosto a posição e zoom iniciais, a palete de cores (consulte padrões [aqui](https://colorbrewer2.org/)) ou outras propriedades do mapa.
3. **Acrescente** informação adicional relevante a cada região do seu mapa, como nome, população total, área, etc. Para isso deve acrescentar colunas ao `GeoDataFrame` (na função `populacaoUcrania`), e mapear o conteúdo dessas colunas na forma de *tooltips* e/ou *popups*; **adapte** o código comentado da função `desenhaRegioesUcrania`. Pode abrir e visualizar o ficheiro `mapa.html` resultante com um browser web à escolha.

## Tarefa 4 (Animações)

O objetivo desta tarefa é analisar o dataset [VIINA](https://github.com/zhukovyuri/VIINA) que contém um registo de eventos militares extraídos de notícias nos mídia referentes ao conflito atual na Ucrânia, atualizado diariamente no ficheiro [events_latest.csv](https://raw.githubusercontent.com/zhukovyuri/VIINA/master/Data/events_latest.csv), e construir uma animação com o `Pygame` que permita visualizar esses mesmos dados.

### 1. Processar dados

Este dataset é automaticamente gerado a partir de informação online de notícias, utilizando algoritmos de aprendizagem por computador que classificam a probabilidade do evento ter certas propriedades, como ter sido iniciado por uma entidade específica. Pode consultar as entidades envolvidas na variável `event_a`.

O primeiro passo é então categorizar cada evento com uma entidade `a`. Para isso deve analisar e agregar os dados das colunas que começam por `a_`, respetivamente, e atribuir um modo `ukr`, `rus` ou `other` consoante a componente com maior probabilidade.
Também vai ser útil converter a coluna `date`num objeto do tipo `datetime64` e a coluna `time` numa coluna `minutes` com o número total de minutos.
**Complete** a definição da função `processaEventos`, que lê o ficheiro [events_latest.csv](../scripts/projeto3/dados/events_latest.csv) com o registo dos eventos para um `DataFrame` e retorna um `DataFrame` com o formato similar ao seguinte (ignore os dados concretos):
```python
         date  longitude   latitude     a   minutes
0    2022-02-24  38.002536  48.306080    ukr       10
1    2022-02-24  37.802850  48.015884  other       11
2    2022-02-25  37.802850  48.015884  other       12
3    2022-02-26  30.523550  50.450441    rus       13
...       ...        ...        ...    ...      ...
```

### 2. Desenhar animação

Vamos utilizar os mapas diários sobre o conflito publicados pelo [Institute for the Study of War](https://www.understandingwar.org/). Podem consultar alguns destes mapas na pasta [maps](../scripts/projeto3/images/maps), cujo nome é referente a um dia e cujo conteúdo realça as zonas de conflito nesse dia. 

A classe `Animacao` facilita o processo de criação de uma animação `Pygame` para esta tarefa:

* O construtor `__init__` cria uma nova animação, carregando um mapa dado e configurando a janela.
* O método `run` corre a animação, com uma dada *framerate* em frames por segundo. Cada frame corresponde a um minuto do dia em animação.
* O método `desenhaFrame` é chamado a cada minuto/frame da animação. **Complete** a sua definição; o método recebe o ecrã, o novo dia/mapa, o minuto/frame atual e um `DataFrame` com os eventos para esse dia/mapa; o seu objetivo é desenhar os eventos referentes ao minuto atual no mapa. **Notas:**
    - Sinalize eventos de forma diferente consoante a entidade a quem pertencem. Pode sinalizar eventos utilizando as imagens, cores, formas geométricas `Pygame` ou qualquer outra marcação que ache interessante.
    - Deve usar os métodos `toX` e `toY` para converter coordenadas de longitude e latitude, respetivamente, em coordenadas `PyGame` no ecrã. Note que estes métodos são uma simplificação que não tem em consideração a curvatura da Terra; para uma maior precisão poderíamos utilizar o `matplotlib`.
    - Se não *limpar* o mapa a cada frame, o comportamente natural será os vários eventos ao longo do tempo se irem acumulando no ecrã à medida que ocorrem. Se *limpar* o mapa a cada frame, apenas os eventos do minuto atual serão visualizados. Qualquer comportamento é aceitável.

### 3. Melhorar animação (Valorização)

Melhore a sua animação, por exemplo de uma das seguintes formas:

* Faça com que cada evento seja visualizado durante um período de tempo ligeiramente maior do que o minuto a que pertence (e.g. incluindo os 2 minutos anteriores e posteriores), e inclua uma animação (e.g., aparece/desaparece, cresce/diminui, muda de cor, etc).
* Acrescente informação de data e tempo ao ecrã.
* Acrescente à animação de cada evento uma indicação visual da precisão geográfica do evento. 
* Acrescente à animação de cada evento uma indicação do tipo de evento.


