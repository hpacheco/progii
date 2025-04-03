# Projeto 2 - Análise de dados

Neste segundo projeto vamos investigar os conceitos base de análise de dados em Python de uma perspetiva prática, e aplicá-los na leitura e processamento de dados em formatos comumente presentes na web.

Aceda aos ficheiros do Projeto 2, onde deve preencher as suas soluções num ficheiro `projeto2.py`:

- Pode consultar os ficheiros individuais na pasta [projeto2](../scripts/projeto2) e fazer download dos mesmos para desenvolver o projeto no seu computador e utilizando um IDE à sua escolha.
- Pode fazer download de todo o projeto como um arquivo zip [aqui](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2Fhpacheco%2Fprogii%2Ftree%2Fmaster%2Fscripts%2Fprojeto2).
- Se o link anterior não funcionar, pode fazer download de todo o repositório git como um arquivo zip [aqui](https://github.com/hpacheco/progii/archive/refs/heads/master.zip).

## Tarefa 1 (JSON)

Nesta tarefa vamos estudar dados do portal [Nextstrain](https://nextstrain.org/), que fornece informação sobre árvores filogenéticas.

Estude o ficheiro [nextclade_sars-cov-2.json](../scripts/projeto2/dados/nextclade_sars-cov-2.json), que contém uma árvore filogenética do vírus SARS-CoV-2. A informação deste ficheiro pode ser visualizada na página [SARS-CoV-2 phylogeny](https://nextstrain.org/nextclade/sars-cov-2). A árvore está representada no formato JSON da seguinte forma:

```
{
  "version": "v2",
  "tree": {
    "name": "NODE_0000000",
    "node_attrs": ...
    "branch_attrs": ...
    "children": [ ... ]
  ...
  }
```

A raiz da árvore, ou seja, a primeira variante conhecida do vírus tem o nome `NODE_0000000`.
Os campos `node_attrs` e `branch_attrs` contêm informação adicional sobre cada variante.
A árvore filogenética é construída anotando cada variante com a lista dos seus descendentes diretos, que são por sua vez variantes/árvores com a mesma estrutura que o campo `tree`.

Explore este ficheiro de dados escrevendo funções Python que respondam às seguintes questões:

* Complete a definição da função `mostRecentStrains`, que retorna um dicionário com as variantes mais recentemente conhecidas (sem descendentes). As chaves do dicionário devem ser os nomes (campo `name`) e os valores a sua divergência em relação à raiz (campo `node_attrs.div`).
* Complete a definição da função `numberDescendantsOf`, que recebe o nome de uma variante atribuído pela organização mundial de saúde (WHO), e retorna o número de descendentes mais recentes dessa variante. Para cada variante, o campo `node_attrs.clade_who.value` (quando definido) contém o nome atribuído pela WHO.
* Complete a definição da função `mostCommonMutation`, que retorna um tuplo com o nome da mutação mais frequente e o respetivo número de mutações. As mutações filogenéticas de uma variante encontram-se descritas no campo `branch_attrs.mutations.nuc`.
* Complete a definição da função `longestEvolutionaryBranches`, que retorna uma árvore de nomes de variantes, contendo apenas as variantes com um historial evolutivo mais longo desde a raiz.

## Tarefa 2 (NumPy)

Um dos problemas mais comuns em bioinformática prende-se com o alinhamento e comparação de sequências. Considere o ficheiro [16SRNA_Deino_87seq.aln.fasta](../scripts/projeto2/dados/16SRNA_Deino_87seq.aln.fasta) de um *multiple sequence alignment* (MSA) retirado [deste](https://www.ncbi.nlm.nih.gov/tools/msaviewer/tutorial1/) tutorial. Em particular, o ficheiro contém várias sequências de proteínas, no formato FASTA, previamente alinhadas.

**Nota:** Por lapso, o ficheiro FASTA dado contém sequências de nucleótidos e não de aminoácidos. Podem resolver o exercício utilizando os 20 aminoácidos, em que grande parte deles vão ter 0 ocorrências, o que está a ocorrer no exemplo dado, ou contabilizar apenas os 5 nucleótidos possíveis `ACGTU`, e calcular uma matrix de $5x5$.

Comece por analisar o resultado da função `readMSA` dada, que lê as respetivas sequências alinhadas de um ficheiro FASTA. Note que todas as sequências têm o mesmo comprimento. Existem precisamente 20 letras de aminoácidos possíveis: `ACDEFGHIKLMNPQRSTVWY`. O caracter `-` denota um *gap*, ou seja, um aminoácido em falta e é utilizado para alinhar sequências originalmente de tamanhos diferentes.

Complete a definição da função `createBLOSUM()`, que cria uma matriz de substituição a partir de um MSA. Pode consultar a entrada sobre o método [BLOSUM](https://en.wikipedia.org/wiki/BLOSUM) na Wikipedia para mais informações. No entanto, vamos assumir algumas simplificações e calcular a matrix de acordo com os seguintes passos:

1. Calcule a frequência de cada aminoácido em todas as sequências. Ignorando *gaps*, a frequência de um aminoácido $A$ é dada por $f(A) = \frac{\text{número de ocorrências do aminoácido}}{\text{número total de aminoácidos}}$.
2. Calcule a probabilidade $P(A,B)$ de dois aminoácidos $A$ e $B$ estarem alinhados em duas sequências, ou seja, $A$ e $B$ aparecerem na mesma posição de sequências de proteínas diferentes. Outra vez ignorando *gaps*, esta probabilidade é dada por $P(A,B) = \frac{\text{número de ocorrências do par (A,B)}}{\text{número total de pares}}$. Note que a ordem dos elementos do par é irrelevante, ou seja, $P(A,B) = P(B,A)$. Desta forma, para uma dada posição existem $\left( \frac{n}{2} \right)$ pares de aminoácidos possíveis (se não houver aminoácidos em falta), onde $n$ é o número de sequências a serem comparadas.
3. Calcule a matrix de substituição $S(A,B) = \log_2 \left( \frac{P(A,B)}{f(A) * f(B)} \right )$, arredondando cada entrada a um valor inteiro. Para o MSA de exemplo, o resultado é a seguinte matrix simétrica de $20x20$:


```
     A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
A [[ 2 -2  0  0  0 -2  0  0  0  0  0  0  0  0  0  0 -2  0  0  0 ]
C  [-2  2  0  0  0 -2  0  0  0  0  0  0  0  0  0  0 -1  0  0  0 ]
D  [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
E  [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
F  [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
G  [-2 -2  0  0  0  2  0  0  0  0  0  0  0  0  0  0 -2  0  0  0 ]
H  [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
I  [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
K  [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
L  [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
M  [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
N  [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
P  [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
Q  [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
R  [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
S  [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
T  [-2 -1  0  0  0 -2  0  0  0  0  0  0  0  0  0  0  2  0  0  0 ]
V  [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
W  [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
Y  [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]]
```

Complete a definição da função `mostSimilarSequences`, que retorna quais os nomes das duas sequências mais similares de acordo com a matrix calculada anteriormente. O *score* de similaridade entre duas sequências pode ser calculado por $\sum_i S(A_i,B_i)$, para todas as posições $i$ na sequência. Considere que $S(-,-)=0$, $S(A,-)=-3$ e $S(-,B)=-3$.

## Tarefa 3 (Pandas)

Considere os dados sobre perdas económicas por fenómenos climatéricos, recolhidos pelo portal da European Environment Agency [aqui](https://www.eea.europa.eu/en/datahub/datahubitem-view/1fac8253-3df7-4408-b5fa-a6f2dc524182), com uma versão local no ficheiro [eea_s_eu-sdg-13-40_p_1980-2023_v03_r00.xlsx](../scripts/projeto2/dados/eea_s_eu-sdg-13-40_p_1980-2023_v03_r00.xlsx)

Explore este conjunto de dados escrevendo programas Python que respondam às seguintes questões:

* Qual o ano em que se registaram mais perdas totais na União Europeia dos 27? Complete a definição da função `piorAnoUE`, que retorna o ano em questão.
* Qual o país (excluindo valores totais da UE) que registou um maior aumento (em proporção) entre os totais de perdas registadas no século XX e no século XXI? Complete a definição da função `paisMaisAgravado`, que retorna o nome do país em questão. Ignore países com pelo menos um dos séculos a `0`.
* Por cada ano, qual a região [EuroVoc](https://en.wikipedia.org/wiki/EuroVoc) mais afetada, considerando número total de perdas? Complete a definição da função `registoAnual`, que retorna um dicionário `{ ano : regiao }`. Deve utilizar a associação de regiões EuroVoc a países fornecida na variável `regioesEuroVoc`.

## Tarefa 4 (NetworkX)

Considere o ficheiro [0014932-250310093411724.csv](../scripts/projeto2/dados/0014932-250310093411724.csv), extraído do portal [Global Biodiversity Information Facility](https://www.gbif.org/dataset/efd57d4b-2a63-477a-a6ea-7211f37e9d66), que contém uma listagem de avistamentos de animais em Portugal. Utilizando a biblioteca `NetworkX`, responda programaticamente às seguintes questões:

* Construa um grafo de co-ocorrências de espécies de morcegos (coluna `order` igual a `Chiroptera`), em que duas espécies estão ligadas por uma aresta se tiveram avistamentos na mesma zona. Dois avistamentos são considerados na mesma zona quando ocorrem com uma distância inferior a 1km. Utilize a função `geodist` dada para calcular a distância em km entre duas coordenadas GPS. Quantos habitats distintos (no sentido em que nenhuma espécie de um habitat foi avistada conjuntamente com uma espécie de outro habitat) de morcegos existem? Complete a definição da função `habitatsMorcegos`.
* Construa um grafo que liga regiões, utilizando como peso o número de espécies que não se encontra em nenhuma das regiões, em relação ao número total de espécies. Qual a melhor escolha de trajeto (sequência de regiões vizinhas) para um corredor de vida selvagem que liga `VianadoCastelo` a `Faro`? Melhor aqui no sentido em que permite proteger uma maior quantidade de espécies. Complete a definição da função `corredorVidaSelvagem`. Deve utilizar a informação sobre que regiões fazem fronteira umas com as outras guardada na variável `regioesVizinhas` dada.



