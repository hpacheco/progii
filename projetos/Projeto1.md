# Projeto 1 - Análise de texto

Neste primeiro projeto vamos relembrar alguns conceitos base da programação em Python e aplicá-los no processamento de ficheiros de texto.

Aceda aos ficheiros do Projeto 1, onde deve preencher as suas soluções num ficheiro `projeto1.py`:

- Pode consultar os ficheiros individuais na pasta [projeto1](../scripts/projeto1) e fazer download dos mesmos para desenvolver o projeto no seu computador e utilizando um IDE à sua escolha.
- Pode fazer download de todo o projeto como um arquivo zip [aqui](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2Fhpacheco%2Fprogii%2Ftree%2Fmaster%2Fscripts%2Fprojeto1).
- Se o link anterior não funcionar, pode fazer download de todo o repositório git como um arquivo zip [aqui](https://github.com/hpacheco/progii/archive/refs/heads/master.zip).

Neste projeto vamos extrair métricas simples do texto da obra *Anecdotes of the Habits and Instinct of Animals* de *Mrs. R. Lee* e analisar sequências de DNA.

Para cada tarefa, o ficheiro dado [main.py](../scripts/projeto1/main.py) contém um conjunto de testes que pode utilizar para validar as suas soluções. No entanto, os testes apenas funcionarão como referência: passar nos testes não implica ter nota máxima, nem falhar os testes implica que a solução esteja errada.

## Parte I - Análise de obras literárias

Considere o ficheiro [anecdotes.txt](../scripts/projeto1/dados/anecdotes.txt), retirado e adaptado do [Project Gutenberg](https://www.gutenberg.org/), que contém o texto integral da obra *Anecdotes of the Habits and Instinct of Animals* de *Mrs. R. Lee*.

### Tarefa 1

Complete a função `leParagrafos` que lê o conteúdo de um ficheiro de texto para uma lista de paragrafos, em que cada parágrafo é uma lista de linhas de texto sem caracteres newline. Parágrafos aparecem separados por linhas em branco no ficheiro de entrada e devem ser concatenados numa só string no resultado, separando cada linha por um espaço.

**NOTA:** Utilize o parâmetro `encoding='utf-8-sig'` para evitar problemas de formatação do texto. 

### Tarefa 2

Complete a definição da função `constroiIndiceAnimais`, que retorna uma lista de pares, em que o primeiro elemento é o título desse capítulo (decomposto num dicionário `{singular : plural }` contendo os animais a que se refere) e o segundo elemento é uma lista de parágrafos que ocorrem por ordem nesse capítulo.

Note que deve ignorar as linhas iniciais que ocorrem antes do primeiro capítulo. Note que os nomes de animais nos títulos dos capítulos se encontram no plural, e pode usar a função dada `singularize` para determinar (quase sempre corretamente) o seu singular. Deve também usar a lista `animals` dada para determinar se uma palavra é um nome de um animal.

### Tarefa 3

Complete as definições das seguintes funções que calculam métricas sobre o texto integral:

- A função `menorCapitulo` que retorna o índice do capítulo com o menor número de parágrafos.
- A função `maiorMonologo` que retorna qual o maior monólogo do texto e o seu respetivo capítulo. Um monólogo é uma sequência de texto delimitada pelo caracter `"`.
- A função `outrasMencoes` que retorna um dicionário `{ animal : menções }`, em que `animal` é um nome singular de um animal que aparece no título de um capítulo e `menções` é o número de menções a esse animal em capítulos dedicados outros animais.
- A função `fleschKincaid` que calcula o [Flesch-Kincaid readability level](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests), amplamente utilizado para determinar a dificuldade de leitura de um texto. Este índice é calculado de acordo com a seguinte fórmula:

$$ 206.835 - 1.015 \left( \frac{\text{\#palavras}}{{\text{\#frases}}} \right) - 84.6 \left( \frac{\text{\#sílabas}}{\text{\#palavras}} \right) $$

O cálculo deste índice é bastante sensível à forma como processem o texto, e será relativamente natural que obtenham valores diferentes dos que se encontram nos testes de referência. Algumas notas:

* Ignore o texto dos títulos de cada capítulo.
* Parta cada parágrafo em frases, considerando os caracteres de separação `.!?`.
* Parta cada frase eme palavras considerando apenas caracteres do alfanuméricos e espaços, ignorando qualquer outro caracter de pontuação.
* Calcule o número de sílabas de cada palavra utilizando a função `syllables` fornecida.

## Parte II - Análise de sequências de DNA

Nesta parte vamos processar sequências de DNA utilizando as bibliotecas base do Python.
Note que este exercício é principalmente pedagógico. Várias bibliotecas como o [BioPython](https://biopython.org/) foram desenvolvidas precisamente para automatizar o processamento avançado e eficiente de sequências de DNA.

### Tarefa 4

Complete a definição da função `leProtenia` que lê uma proteína no formato [FASTA](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=BlastHelp).
Um exemplo de uma proteína encontrada no ser humano, com o código [P68871.2](https://www.ncbi.nlm.nih.gov/nuccore/P68871.2?report=fasta&log$=seqview), pode ser consultada na base de dados do [National Center for Biotechnology Information](https://www.ncbi.nlm.nih.gov/). Encontra uma versão local [aqui](../scripts/projeto1/dados/P68871.2.fasta), que inclui o pequeno excerto:

```
>sp|P68871.2|HBB_HUMAN RecName: Full=Hemoglobin subunit beta; AltName: Full=Beta-globin; AltName: Full=Hemoglobin beta chain; Contains: RecName: Full=LVV-hemorphin-7; Contains: RecName: Full=Spinorphin
MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLG
```

A primeira linha do ficheiro contém um cabeçalho com uma pequena descrição.
As seguintes linhas formam uma string que codifica a sequência de aminoácidos que constituem a proteína, sendo cada aminoácido representado por uma letra maiúscula diferente.

O resultado da função deve ser um tuplo, cujo primeiro elemento é o cabeçalho do ficheiro, e o segundo elemento é a sequência de aminoácidos.

### Tarefa 5

Complete a definição da função `findMotifs` que recebe uma proteína (lida na tarefa anterior) e retorna uma sequência de *motifs*, subsequências da cadeia de aminoácidos da proteína que tipicamente desempenham uma dada função biológica.

A ideia da função `findMotifs` é replicar parte da funcionalidade do [PROSITE](https://prosite.expasy.org/), que pode utilizar para desenvolver uma intuição do comportamento esperado desta tarefa.
O resultado deve ser uma listagem de todos os *motifs* encontrados na sequência original.
Para identificar os *motifs*, vamos utilizar a [base de dados do PROSITE](../scripts/projeto1/dados/P68871.2.fasta), com uma cópia disponível no ficheiro [prosite.dat](../scripts/projeto1/dados/prosite.dat). Cada entrada na base de dados tem o seguinte formato:

```
ID   ASN_GLYCOSYLATION; PATTERN.
AC   PS00001;
DT   01-APR-1990 CREATED; 01-APR-1990 DATA UPDATE; 01-APR-1990 INFO UPDATE.
DE   N-glycosylation site.
PA   N-{P}-[ST]-{P}.
CC   /SITE=1,carbohydrate;
CC   /SKIP-FLAG=TRUE;
CC   /VERSION=1;
PR   PRU00498;
DO   PDOC00001;
```

Vamos ter particular interesse nos campos:

* `AC`: o identificador científico do *motif*
* `PA`: um padrão que determina as várias possíveis sequências de aminoácidos que constituem o *motif*. Pode encontrar a notação PROSITE para tais padrões na Wikipedia: [sequence motif notation](https://en.wikipedia.org/wiki/Sequence_motif). Note que o caracter `-` é só para legibilidade do padrão e deve ser ignorado na leitura da sequência.
* `CC`: um campo de comentários, no qual só vamos ter interesse nos metadados `SITE`, que indicam a posição relativa no *motif* em que um dado aminoácido ocorre e a sua função.

Para a proteína de exemplo, o resultado da tarefa deve ser uma string também no formato FASTA com a seguinte informação:

```
>sp|P68871.2|HBB_HUMAN|PA [AC=PS00006] [SITES=1,phosphorylation] [location=5..8]
TPEE
>sp|P68871.2|HBB_HUMAN|PA [AC=PS00005] [SITES=1,phosphorylation] [location=39..41]
TQR
>sp|P68871.2|HBB_HUMAN|PA [AC=PS00006] [SITES=1,phosphorylation] [location=45..48]
SFGD
...
```

Pode constatar que cada *motif* vai corresponder a duas linhas no output, a primeira descrevendo alguma meta-informação, e a segunda a subsequência da proteína original correspondente. Em particular, o campo `location` no resultado deve conter as posições inicial e final da sequência original onde o motif começa e acaba, inclusive.
Note que, por convenção, posições em sequências de proteínas começam no número `1`.
Os resultados devem aparecer ordenados por ordem crescente de coordenadas de `location`.

### Tarefa 6

Para evitar uma dependência da Tarefa 5, nesta tarefa vamos utilizar ficheiros FASTA, por exemplo [P68871.2.motifs.fasta](../scripts/projeto1/dados/P68871.2.motifs.fasta) para a proteína de exemplo anterior, que contêm uma lista de *motifs*.

Complete a definição de duas funções, que recebem uma listagem de *motifs* e representam tarefas essenciais para identificar regiões funcionais críticas em proteínas:

- A função `overlappingMotifs`, que retorna uma string no mesmo formato FASTA, mas em que *motifs* que se sobrepõem (mesmo que parcialmente) aparecem combinados na mesma entrada. O resultado deve aparecer ordenado por ordem decrescente de número de *motifs* e de seguida por `location`. Para a proteína de exemplo, o resultado será:

```
>sp|P68871.2|HBB_HUMAN|PA [ACS=PS00008,PS00006] [location=84..91]
GTFATLSE
>sp|P68871.2|HBB_HUMAN|PA [ACS=PS00006] [location=5..8]
TPEE
...
```

- A função `mostFrequentSites`, que retorna um dicionário que mapeia funções de *sites* numa lista de posições onde esses sites ocorrem na proteína. Para a proteína de exemplo, o resultado será (ignorando ordem):

```
{'phosphorylation': [5, 39, 45, 50, 88], 'amidation': [64], 'myristyl': [84, 137]}
```

