# Projeto 2 - Análise de dados

Neste segundo projeto vamos investigar os conceitos base de análise de dados em Python de uma perspetiva prática, e aplicá-los na leitura e processamento de dados em formatos comunmente presentes na web.

Aceda ao repositório [replit](https://replit.com/@up652136/Prog2-Proj2) do Projeto 2, onde pode encontrar um ficheiro `projeto2.py`:

- Criando uma conta no [replit](https://replit.com/) e fazendo `Fork` do projeto, pode resolver o projeto online utilizando o IDE web.
- Pode também fazer download dos ficheiros na pasta [projeto2](../scripts/projeto2) para desenvolver o projeto no seu computador e utilizando um IDE à sua escolha.

## Tarefa 1 (JSON)

Observe o JSON ficheiro [nuclear_power_plants.json](../scripts/projeto2/dados/nuclear_power_plants.json), retirado [daqui](https://github.com/cristianst85/GeoNuclearData/blob/master/data/json/denormalized/nuclear_power_plants.json), que contém uma listagem das centrais nucleares existentes no planeta.
Pode ler o conteúdo do ficheiro JSON para uma estrutura de dados em Python da seguinte forma:
```python
import json
with open('nuclear_power_plants','r') as f: str = f.read()
dados = json.loads(str)
```
O resultado guardado na variável `dados` será uma lista de centrais nucleares, em que cada central é representada por um dicionário com campos como o seu nome, o seu país ou a sua geolocalização.

Explore este conjunto de dados escrevendo programas Python que respondam às seguintes questões:

* Qual o país com maior capacidade acumulada de energia nuclear? Considere apenas estações com estado operacional. Complete a definição da função `paisMaisNuclear`.
* Qual o tipo de reator cuja média de anos de construção da central é mais recente? Complete a definição da função `reatorMaisRecente`.
* Qual o país com 3 das centrais com maior capacidade? Procure centrais por ordem decrescente de capacidade até encontrar 3 do mesmo país. Complete a definição da função `paisTresMaioresCentrais`.
* Quantas centrais nucleares existem num raio de 500km de Paris? Calcule a distância em km entre duas geolocalizações utilizando a função `geodist` e sabendo que Paris tem latitude `48.8703520765571` e longitude `2.3466898684084248`. Complete a definição da função `centraisParis`. 

## Tarefa 2 (GeoJSON)

De forma a visualizar mais facilmente os dados, defina a função `formataCentrais(f,centrais)` que recebe uma função `f` que formata cada central, uma lista de dados de centrais e a converte no formato GeoJSON, aplicando a `f` a cada central da lista de centrais recebida.
O formato GeoJSON é JSON válido, e segue uma estrutura específica para representar marcadores geográficos e metadados associados. 
Por exemplo, uma estrutura só com um ponto deverá ter o seguinte formato (como o campo features é uma lista suporta múltiplos pontos).
```python
{
    "type": "FeatureCollection", 
    "features": [
        {
            "geometry": {
                "type": "Point", 
                "coordinates": [
                    float com valor de longitude, 
                    float com valor de latitude
                ]
            }, 
            "type": "Feature", 
            "properties": um dicionário com a metainformação associada ao ponto geográfico
            }
        }]
}
```
Coloque toda a metainformação da central nas propriedades de cada central.
Para organizar melhor o código, defina e utilize uma função auxiliar `formataCentral(central)` que converte uma `central` num feature GeoJSON.
Guarde a lista de centrais resultante num ficheiro GEOJSON `centrais.geojson` utilizando o seguinte código:
```python
geodados = formataCentrais(formataCentral,dados)
with open('centrais.geojson', 'w') as f:
  json.dump(geodados,f)
```
Pode facilmente visualizar o ficheiro resultante num mapa interativo e inspecionar a sua meta-informação em <https://geojson.io/>.

Explore as propriedades de cada marcador que o formato GeoJSON suporta em <https://geojson.io/>.
Defina a função `formataCentralEstilo` que altera as propriedades de cada marcador utilizando:

* uma cor diferente por cada país
* um símbolo diferente por cada tipo de reator. Consulte a lista de símbolos [aqui](https://map.michelstuyts.be/icons/).

Grave e observe o resultado estilizado:
```python
geodados2 = formataCentrais(formataCentralEstilo,dados)
with open('centrais2.geojson', 'w') as f:
  json.dump(geodados2,f)
```

## Tarefa 3 (NumPy)

Faça download para uma pasta local do ficheiro CSV [nuclear_country_year.csv](../scripts/projeto2/dados/nuclear_country_year.csv), adaptado [deste](https://github.com/owid/energy-data) repositório, que contém estatísticas de energia nuclear gerada (como percentagem da energia total gerada) por cada país ao longo dos anos desde 1960 até 2014.

Este ficheiro CSV é essencialmente uma matriz de valores numéricos, que pode ser lida para um array 2D utilizando a biblioteca numpy da seguinte forma.
```python
import numpy as np
dados3 = np.genfromtxt('dados/nuclear_country_year.csv',delimiter=',',filling_values=0)
```
Repare que os campos não numéricos, como nomes de países, são convertidos no valor `0` por defeito.
Dessa forma. o `numpy` não é muito conveniente para ler dados não numéricos, o que no entanto é possível se alterarmos o tipo de dados de todas as colunas. Uma forma de ler apenas a primeira coluna com os nomes dos países seria a seguinte:
```python
paises3 = np.genfromtxt('dados/nuclear_country_year.csv',delimiter=',',dtype=object,usecols=[0])
```

Explore este conjunto de dados escrevendo programas Python que respondam às seguintes questões:

* Quantas vezes um país ultrapassou a meta dos `30%` de energia nuclear gerada num ano? Complete a definição da função `trintaPorCento`.
* Qual o ano em que, em média de todos os países, houve uma maior percentagem de energia nuclear gerada? Complete a definição da função `anoMaisNuclear`.
* Por década, quantos países produziram energia nuclear? O resultado deve ser uma lista de inteiros por ordem crescente de década. Complete a definição da função `nuclearDecadas`.
* Que países abandonaram a energia nuclear? Retorne uma sequência com os nomes dos países. Complete a definição da função `naoMaisNuclear`.

## Tarefa 4 (Pandas)

Faça download para uma pasta local do ficheiro CSV [owid-energy-data.csv](../scripts/projeto2/dados/owid-energy-data.csv), retirado [deste](https://github.com/owid/energy-data) repositório, que contém estatísticas de energia gerada por cada país mundial.
Carregue este ficheiro para um `DataFrame` utilizando o `pandas`:
```python
dados4 = pd.read_csv('dados/owid-energy-data.csv')
```

Explore este conjunto de dados escrevendo programas Python que respondam às seguintes questões:

* Qual o país que teve maior percentagem de energias renováveis em 2020 e com que percentagem? Complete a definição da função `maisRenovaveis2020`, que retorna um par (país,percentagem).
* Qual a preponderância de cada tipo de energia em Portugal em 2020? Retorne uma lista de pares `(tipo,percentagem)` por ordem decrescente de percentagens, em que cada tipo é um elemento da lista `['gas','coal','nuclear','oil','solar','wind','hydro','other_renewables']`. Complete a definição da função `energiaPortugal2020`.
* Qual o país do mundo mais dependente de carvão, para cada ano? Ignore países e anos para os quais não existem dados. Complete a definição da função `maisDependentesCarvao`. O resultado deve ser um dicionário `{ ano : país }`.
* Qual a média, para cada país da União Europeia, de percentagem de dependência de gás entre 1990 e 2021? Utilize a listagem de países `eu_countries`. Complete a definição da função `gasUE`. O resultado deve ser um dicionário `{ ano : média }`.

## Tarefa 5 (Pandas) (Valorização)

Faça download para uma pasta local do ficheiro CSV [portdata-energy-import.xlsx](../scripts/projeto2/dados/pordata-energy-import.xlsx), retirado do [PORDATA](https://www.pordata.pt/en/Europe/Energy+import+dependency-3601), que contém estatísticas de percentagem de energia importada para países da União Europeia.

Pode ler os dados para um `DataFrame` com o comando:
```python
dados5 = pd.read_excel('dados/pordata_energy_import.xlsx',sheet_name='Table')
```

Cruze estes dados com a tabela de dados de energia mundial da Tarefa 4, de forma a responder programaticamente às seguintes questões:

* Para cada país da União Europeia listado nos `dados5`, qual o ano em que importou menos menos energia não renovável? Ignore dados de anos em falta. Complete a definição da função `anoMaisRenovavelEU`.


