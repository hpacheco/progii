# Projeto 1 - Análise de texto

Neste primeiro projeto vamos relembrar alguns conceitos base da programação em Python e aplicá-los no processamento de ficheiros de texto.

Aceda ao repositório [replit](https://replit.com/@up652136/Prog2-Proj1) do Projeto 1, onde pode encontrar um ficheiro `projeto1.py`:
- Criando uma conta no [replit](https://replit.com/) e fazendo `Fork` do projeto, pode resolver o projeto online utilizando o IDE web.
- Pode também fazer download dos ficheiros na pasta [projeto1](../scripts/projeto1) para desenvolver o projeto no seu computador e utilizando um IDE à sua escolha.

Neste projeto vamos processar o texto completo do *Sermão de Santo António aos Peixes* do *Padre António Vieira*, extrair métricas simples e reformatar o texto.

## Tarefa 1

Faça download para uma pasta local do ficheiro [sermao.txt](../scripts/projeto1/dados/sermao.txt), que contém o texto integral do *Sermão de Santo António aos Peixes* do *Padre António Vieira*.

Complete a função `leTexto` que lê o conteúdo de um ficheiro de texto para uma lista de linhas de texto, em que cada linha de texto é uma string sem caracteres newline.

## Tarefa 2

Analise a definição da função ``organizaSermao`` que organiza uma lista de linhas de texto num tuplo (título,introdução,lista de capítulos), em que cada capítulo é um tuplo (número,lista de parágrafos). Cada linha do título, introdução e parágrafo é por sua vez uma lista de palavras (com pontuação).
Por exemplo, para um sermão dado como a lista de linhas:
```python
['SERMÃO DE EXEMPLO'
,''
,'A título de exemplo.'
,'Veni, vidi, vici.'
,''
,'I'
,''
,'Parágrafo um.'
,'Parágrafo dois.'
]
```
O resultado organizado esperado é:
```python
(['SERMÃO','DE','EXEMPLO'],[['A','título','de','exemplo.'],['Veni,','vidi,','vici.']],[('I',[['Parágrafo','um.'],['Parágrafo','dois.']])])
```

Complete as seguintes definições auxiliares:
- A função `separaLinha` que parte uma linha (string sem newlines) numa lista de palavras;
- A função `separaLinhas`, que parte uma lista de linhas numa lista de listas de linhas, usando como delimitador strings vazias;
- A função `organizaCapitulos`, que recebe uma lista de de listas de linhas correspondente ao texto (sem linhas em branco) dos capítulos de um sermão e retorna uma lista de capítulos como descrito em cima.

# Tarefa 3

Complete as definições das seguintes funções, que recebem como argumento um sermão organizado como descrito na Tarefa 2.
- A função `totais` que retorna um tuplo com os números totais de capítulos, parágrafos e palavras (todas as palavras do texto, incluindo título, descrição e capítulos);
- A função `deusPeixes` que retorna quantas vezes as palavras 'Deus' e 'peixes' ocorrem no mesmo parágrafo;
- A função `maiorParagrafo` que retorna o nome do capítulo com maior média de palavras por parágrafo. Caso haja mais do que um capítulo com a maior média, deverá retornar a primeira ocorrência. Assuma que a média de um capítulo sem parágrafos é 0.

# Tarefa 4

Faça download para uma pasta local dos ficheiros [la.txt](../scripts/projeto1/dados/la.txt) e [pt.txt](../scripts/projeto1/dados/pt.txt), que contêm dois dicionários que consistem em listas exaustivas de palavras em Latim e em Português. 

Analise o código que lê o conteúdo dos ficheiros para dois ``set``s de palavras `la_dic` e `pt_dic`.
Dada uma palavra normalizada (sem pontuação nem maiúsculas), podemos definir facilmente a função `spellcheck` que verifica se uma palavra dada está em algum dos dicionários.

Complete a função `normalizaPalavra` que recebe uma string sem espaços e retira pontuação (qualquer caracter não alfanumérico) **apenas** no início e no fim da palavra e converte todos os caracteres em minúsculas, retornando um tuplo (prefixo,palavra original,palavra normalizada,sufixo). Por exemplo:
```python
normalizaPalavra('-Normalizá-lo-ei!!')
```
Deve retornar:
```python
('-','Normalizá-lo-ei','normalizá-lo-ei','!!')
```

# Tarefa 5

Complete a função ``formataSermao`` que recebe como argumento um sermão organizado como descrito na Tarefa 2 e retorna uma string no formato [Markdown](https://www.markdownguide.org/basic-syntax/). Por exemplo, para o sermão:
```python
(['SERMÃO','DE','EXEMPLO'],[['A','título','de','exemplo,','Blah!'],['Veni,','vidi,','vici.']],[('I',[['Parágrafo','um.'],['Parágrafo','dois.']])])
```
A string resultante deverá ter a seguinte formatação:
```python
# SERMÃO DE EXEMPLO
> A título de exemplo, ~~Blah~~!
> 
> *Veni*, *vidi*, *vici*.

## I
Parágrafo um.

Parágrafo dois.
```
O formato [Markdown](https://www.markdownguide.org/basic-syntax/) suporta uma sintaxe especial de texto para definir títulos, estilos de letra e outras formatações; consulte a documentação. Pode visualizar o texto formatado utilizando escrevendo o seu conteúdo para um ficheiro com extensão `.md`, por exemplo `sermao.md` e utilizar a pré-visualização automática do IDE. Pode também copiar o texto para um pré-visualizador web como [este](https://markdownlivepreview.com/)

Neste exemplo, o título aparece formatado como Título 1, e cada capítulo como Título 2. Cada parágrafo encontra-se separado por uma linha em branco. Os parágrafos da descrição encontram-se formatados como um só bloco de citação.
Cada palavra do texto também se encontra formatada de acordo com o resultado da função ``spellcheck``(para a palavra normalizada) definida acima:
* palavras no dicionário Português não têm qualquer formatação;
* palavras no dicionário Latim encontram-se em *itálico*;
* palavras que não se encontrem em nenhum dos dicionários encontram-se ~~rasuradas~~.
Repare que apenas a palavra original (excluindo caracteres de pontuação) se encontra formatada.
Para isso, é útil definir a função auxiliar `formataPalavra`, que deve receber uma palavra, normalizá-la, correr o spellchecker e retornar a palavra formatada. Por exemplo, para uma palavra em Inglês:
```python
formataPalavra('English?')
```
Deve retornar a palavra rasurada:
```python
~~English~~?
```


