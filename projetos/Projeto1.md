# Projeto 1 - Análise de texto

Neste primeiro projeto vamos relembrar alguns conceitos base da programação em Python e aplicá-los no processamento de ficheiros de texto.

Aceda aos ficheiros do Projeto 1, onde deve preencher as suas soluções num ficheiro `projeto1.py`:

- Fazendo login no [replit](https://replit.com/) com a conta Google UP (upXXXXX@g.uporto.pt), acendendo à Team [prog2bio2324](https://replit.com/team/prog2bio2324) e iniciando o Projeto1.
- Pode consultar os ficheiros individuais na pasta [projeto1](../scripts/projeto1) e fazer download dos mesmos para desenvolver o projeto no seu computador e utilizando um IDE à sua escolha.
- Pode fazer download de todo o projeto como um arquivo zip [aqui](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2Fhpacheco%2Fprogii%2Ftree%2Fmaster%2Fscripts%2Fprojeto1).

Neste projeto vamos extrair métricas simples do texto completo da obra *A Relíqua* de *Eça de Queiroz* e analisar sequências de DNA.

## Parte I - Análise de obras literárias

Considere o ficheiro [cidadeserras.txt](../scripts/projeto1/dados/cidadeserras.txt), retirado e adaptado do [Project Gutenberg](https://www.gutenberg.org/), que contém o texto integral da obra *A Cidade e as Serras* de *Eça de Queiroz*.

### Tarefa 1

Complete a função `leParagrafos` que lê o conteúdo de um ficheiro de texto para uma lista de paragrafos, em que cada parágrafo é uma lista de linhas de texto sem caracteres newline. Parágrafos aparecem separados por linhas em branco no ficheiro de entrada e devem ser concatenados numa só string no resultado, separando cada linha por um espaço. **NOTA:** Utilize o parâmetro `encoding='utf-8-sig'` para evitar problemas de formatação do texto. 

### Tarefa 2

Complete a definição da função `organizaCapitulos`, que retorna um dicionário que mapeia capítulos numa lista de parágrafos que ocorrem por ordem nesse capítulo. Note que deve ignorar as linhas iniciais que ocorrem antes do primeiro capítulo.

### Tarefa 3

Complete as definições das seguintes funções que calculam métricas sobre o texto integral da obra *A Cidade e as Serras* de *Eça de Queiroz*:

- A função menorCapitulo que retorna qual o capítulo com menor número de caracteres. O tamanho de cada capítulo é a soma todos os caracteres dos seus parágrafos.
- A função `maiorDialogo` que retorna o tamanho da maior sequência de monólogos consecutivos. Deve considerar que um monólogo é um parágrafo que se inicia com `--'.
- A função `mencoesPersonagens` que recebe um conjunto de nomes de personagens, e retorna o número de parágrafos que mencionam todas as personagens, por capítulo, com os capítulos ordenados primeiro por ordem decrescente de menções e segundo por número do capítulo.
- A função `ohJacinto` que retorna um conjunto de monólogos endereçados ao Jacinto, personagem principal da obra. Deve considerar que um monólogo se endereça ao Jacinto quando o monólogo contém uma frase que contém a palavra `Jacintho` e que acaba em `!` ou em `?`. Cada frase termina num caracter de pontuação `.`, `!` ou `?`.

## Parte II - Análise de sequências de DNA

Nesta parte vamos processar sequências de DNA utilizando as bibliotecas base do Python.
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

Complete a definição da função `encontraProteinas` que recebe uma sequência de DNA no sentido $5' \rightarrow 3'$ e traduz numa sequência de aminoácidos de forma a encontrar proteínas. 

Para fazer a tradução, deve utilizar o [código genético standard](https://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=tgencodes#SG1) disponibilizado no ficheiro [standard_code.1]() e que consiste em:

```
    AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ---M------**--*----M---------------M----------------------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
```

Cada coluna determina uma proteína. As linhas `Base1` a `Base3` define um *codon*, 3 bases que formam um aminoácido, com nome na linha `AAs`. A linha `Starts` determina os *codons* de início (marcados com `M`) e de fim (marcados com `*`) de uma proteína.

A ideia da função `encontraProteinas` é replicar parte da funcionalidade do [ORF Finder](https://www.ncbi.nlm.nih.gov/orffinder/), que pode utilizar para desenvolver uma intuição do comportamento esperado desta tarefa.
O resultado deve ser uma listagem de todas as proteínas encontradas na sequência original, em que cada proteína encontrada é um tuplo com a posição da primeira base do *codon* de início, a posição da última base do *codon* de fim e a sequência de aminoácidos da proteína (sem o `*` terminal), respetivamente. Note que, por convenção posições em sequências de proteínas começam no número `1`.

A função dada `orfFinder` aplica a função `encontraProteinas` nas duas sequências de uma cadeia de DNA, quer na sequência $5' \rightarrow 3'$, quer na sequência complemento $3' \rightarrow 5'$. Note que a pesquisa de proteínas na sequência complemento é feita no sentido $5' \rightarrow 3'$, ou seja, da direita para a esquerda neste caso; as posições são no entanto na mesma da esquerda para a direita. O resultado é uma listagem de proteínas, em que cada tuplo tem mais um elemento `"+"` ou `"-"` consoante a proteína tenha sido encontrada na sequência original ou no seu complemento, respetivamente.

### Tarefa 6

Complete a função `intergenicRegions` que recebe uma cadeia de DNA e retorna uma listagem das regiões entre genes, tanto na sequência original como no seu complemento.
Para evitar uma dependência da Tarefa 5, esta função recebe como parâmetro adicional um ficheiro FASTA, por exemplo [U49845.1.cds](../scripts/projeto1/dados/U49845.1.cds.fasta) para o fungo de exemplo anterior, que inclui as *coding sequences* (CDS) encontradas, ordenadas por posição, como no excerto:

```
>lcl|U49845.1_cds_AAA98665.1_1 [protein=TCP1-beta] [frame=3] [protein_id=AAA98665.1] [location=<1..206] [gbkey=CDS]
TCCTCCATATACAACGGTATCTCCACCTCAGGTTTAGATCTCAACAACGGAACCATTGCCGACATGAGAC
...
>lcl|U49845.1_cds_AAA98666.1_2 [gene=AXL2] [protein=Axl2p] [protein_id=AAA98666.1] [location=687..3158] [gbkey=CDS]
ATGACACAGCTTCAGATTTCATTATTGCTGACAGCTACTATATCACTACTCCATCTAGTAGTGGCCACGC
...
>lcl|U49845.1_cds_AAA98667.1_3 [gene=REV7] [protein=Rev7p] [protein_id=AAA98667.1] [location=complement(3300..4037)] [gbkey=CDS]
ATGAATAGATGGGTAGAGAAGTGGCTGAGGGTATACTTAAAATGCTACATTAATTTGATTTTATTTTATA
...
```

Estamos interessados no campo `location` de cada CDS; os símbolos `<` e `>` que podem aparecer nas posições indicam matches parciais de proteínas, detalhe que vamos ignorar. Note que proteínas encontradas na sequência complemento são indicadas como o complemento das posições da esquerda para a direita na sequência original. Neste caso, existe portanto uma única *intergenic region*, que vamos representar também no formato FASTA:

```
>lcl|U49845.1_cds_AAA98665.1_1..lcl|U49845.1_cds_AAA98666.1_2 [location=207..686] +
...
```

Note que apenas consideramos código genético entre genes, e não no início/fim da sequência; isto faz com que sejam necessários pelo menos dois CDS para existir uma *intergenic region*, como acontece na sequência original de exemplo mas não no seu complemento.

