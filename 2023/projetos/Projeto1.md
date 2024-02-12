# Projeto 1 - Análise de texto

Neste primeiro projeto vamos relembrar alguns conceitos base da programação em Python e aplicá-los no processamento de ficheiros de texto.

Aceda aos ficheiros do Projeto 1, onde deve preencher as suas soluções num ficheiro `projeto1.py`:

- Fazendo login no [replit](https://replit.com/) com a conta Google UP (upXXXXX@g.uporto.pt), acendendo à Team [prog2bio2223](https://replit.com/team/prog2bio2223) e iniciando o Projeto1.
- Pode consultar os ficheiros individuais na pasta [projeto1](../scripts/projeto1) e fazer download dos mesmos para desenvolver o projeto no seu computador e utilizando um IDE à sua escolha.
- Pode fazer download de todo o projeto como um arquivo zip [aqui](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/hpacheco/progii/tree/master/scripts/projeto1).

Neste projeto vamos extrair métricas simples do texto completo da obra *A Relíqua* de *Eça de Queiroz* e analisar sequências de DNA.

## Parte I - Análise de obras literárias

Considere o ficheiro [areliquia.txt](../scripts/projeto1/dados/areliquia.txt), que contém o texto integral da obra *A Relíqua* de *Eça de Queiroz*.

### Tarefa 1

Complete a função `leTexto` que lê o conteúdo de um ficheiro de texto para uma lista de linhas de texto, em que cada linha de texto é uma string sem caracteres newline. **NOTA:** Utilize o parâmetro `encoding='utf-8'` para evitar problemas de formatação do texto. 

### Tarefa 2

Complete a definição da função `constroiIndice`, que retorna uma string com um índice de capítulos para linhas no ficheiro original, com o seguinte formato (repare no alinhamento vertical; as linhas impressas no ecrã devem ter todas o mesmo comprimento, mas os números exatos de espaços ou hífens por linha ficam ao critério dos alunos):

```
I ------ 130
II ---- 2209
...
```

### Tarefa 3

Complete as definições das seguintes funções que calculam métricas sobre o texto integral da obra *A Relíqua* de *Eça de Queiroz*:

- A função `totais` que retorna um tuplo com os números totais de capítulos, parágrafos (incluindo o prefácio mas ignorando o título e marcadores de capítulos) e palavras (todas as palavras do texto, incluindo título, prefácio e capítulos);
- A função `maisFrequente` que retorna um tuplo com a palavra com pelo menos 8 caracteres que mais vezes aparece no texto e o seu respetivo número de ocorrências;
- A função `camisinhaMary` que retorna quantas vezes as palavras 'camisinha' e 'Mary' ocorrem no mesmo parágrafo;
- A função `menorCapitulo` que retorna o nome do capítulo com a menor média de palavras por parágrafo.

**NOTA:** Utilize a função pré-definida `normalizaPalavra` que normaliza uma palavra, removendo capitalização e caracteres de pontuação. 

## Parte II - Análise de sequências de DNA

Nesta parte vamos cortar sequências de DNA de acordo com restrições de enzimas, utilizando as bibliotecas base do Python.
Note que este exercício é principalmente pedagógico. Várias bibliotecas como o [BioPython](https://biopython.org/) foram desenvolvidas precisamente para automatizar o processamento avançado e eficiente de sequências de DNA.

### Tarefa 4

Complete a definição da função `leDNA` que lê uma sequência de DNA no formato [FASTA](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=BlastHelp).
Um exemplo de uma sequência de DNA de um fungo de fermento, com o código [U49845.1](https://www.ncbi.nlm.nih.gov/nuccore/U49845.1?report=fasta&log$=seqview), pode ser consultada na base de dados do [National Center for Biotechnology Information](https://www.ncbi.nlm.nih.gov/). Encontra uma versão local [aqui](../scripts/projeto1/dados/U49845.1.fasta), que inclui o pequeno excerto:

```
>U49845.1 Saccharomyces cerevisiae TCP1-beta gene, partial cds; and Axl2p (AXL2) and Rev7p (REV7) genes, complete cds
GATCCTCCATATACAACGGTATCTCCACCTCAGGTTTAGATCTCAACAACGGAACCATTGCCGACATGAG
```

A primeira linha do ficheiro contém um cabeçalho com uma pequena descrição.
As seguintes linhas formam uma string que codifica a sequência de DNA, contendo quatro bases possíveis codificadas com as seguintes letras:

| letra |   base   | 
|:-----:|:--------:|
| A     | adenine  |
| C     | cytosine |
| G     | guanine  |
| T     | thymine  |

O resultado da função deve ser um par de strings que forma uma [cadeia de DNA](https://www.genome.gov/genetics-glossary/Base-Pair), em que a primeira string é a sequência $5' \rightarrow 3'$ lida do ficheiro, e a segunda string é o complemento $3' \rightarrow 5'$, que pode ser calculada aplicando a função `nucleotidePair` a cada letra da primeira string.

### Tarefa 5

Complete a definição da função `leEnzima` que lê uma lista de restrições de enzimas no formato [staden](https://extras.csc.fi/staden/doc/manual/formats_unix_23.html).
Pode encontrar uma listagem de enzimas neste formato na base de dados [REBASE](http://rebase.neb.com/rebase/link_staden). Encontra uma versão local [aqui](../scripts/projeto1/dados/link_staden.txt), que inclui o pequeno excerto:

```
AanI/TTA'TAA//
AarI/CACCTGCNNNN'NNNN/'NNNNNNNNGCAGGTG//
```

Depois de um cabeçalho de algumas linhas, cada linha define uma enzima no formato `nome/cut53/cut35//`, em que `cut53` e `cut35` são padrões de excertos de DNA nos sentidos $5' \rightarrow 3'$ e $3' \rightarrow 5'$ que compõe a enzima. Estes padrões podem ser as bases `ACGT`, ou as seguintes letras que determinam várias opções de bases:

| letra |   base           | 
|:-----:|:----------------:|
| Y     | C ou T           |
| R     | A ou G           |
| W     | A ou T           |
| S     | G ou C           |
| K     | T ou G           |
| M     | C ou A           |
| D     | A ou G ou T      |
| V     | A ou C ou G      |
| V     | A ou C ou G      |
| H     | A ou C ou T      |
| B     | C ou G ou T      |
| X     | A ou T ou G ou C |
| N     | A ou T ou G ou C |

A variável `nucleotideBases` representa esta tabela como um dicionário.

Cada excerto pode conter um caracter especial `'` que determina a posição particular em que a enzima corta uma sequência de DNA; quando uma posição de corte não é definida concretamente, a posição de corte assumida é no fim do excerto no sentido $5' \rightarrow 3'$ e no início no sentido $3' \rightarrow 5'$. Quando o excerto `cut35` não é dado explicitamente, este pode ser calculado utilizando a função `nucleotidePair`, e a sua posição de corte é o inverso da posição de corte do excerto `cut53`, i.e., contar o mesmo índice da direita para a esquerda.

O resultado da função `leEnzima` deve ser uma base de dados de enzimas, representada como um dicionário de nomes de enzimas para representações de enzimas no formato `(excerto53,pos53,excerto35,pos35)`, em que `excerto53` e `excerto35` são excertos de DNA e `pos53` e `pos35` são respetivamente as posições de corte em cada excerto.

### Tarefa 6

Complete a função `oneCutters` que recebe um dicionário de enzimas e uma cadeia de DNA, e determina quais as enzimas que têm exatamente uma possibilidade de corte da cadeia de DNA. A ideia é replicar parte da funcionalidade do [NEBcutter](https://nc3.neb.com/NEBcutter). O resultado deve ser um dicionário de nomes de enzimas para um tuplo `(pos53,pos35)` que determina as posições em que a enzima corta a cadeia de DNA nos dois sentidos.


