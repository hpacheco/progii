import pandas as pd
import holoviews as hv
from holoviews import opts, dim

# processa os dados

edges = pd.read_excel('eurovision_song_contest_1957_2023.xlsx',usecols=[2,3,4,5,6])
# focus on the 2023 final and on jury votes greater than 10
edges = edges[edges['Edition'] == '2023f']
#del edges['Year']
#del edges['(semi-) final']
del edges['Edition']
#del edges['Duplicate']
edges = edges[edges['Jury or Televoting'] == 'J']
del edges['Jury or Televoting']
edges.columns = ['source','target','value']
edges = edges[edges['value'] >= 10]

print(edges.info())
print(edges)

countries = set(edges['source']).union(set(edges['target']))

nodes = pd.DataFrame(countries,columns=['Country'])
nodes.set_index('Country',inplace=True)
nodes['Region'] = 'Outside of Europe'
nodes['Color'] = 'grey'

# EuroVoc EU regions
regions = {
    'Central and Eastern Europe':
        ('red',[ 'Albania', 'Armenia', 'Azerbaijan', 'Belarus', 'Bosnia and Herzegovina', 'Bulgaria', 'Czech Republic', 'Croatia', 'Georgia', 'Hungary', 'Moldova', 'Montenegro', 'North Macedonia', 'Poland', 'Romania', 'Russia', 'Serbia', 'Slovakia', 'Slovenia', 'Ukraine']),
    'Northern Europe':
        ('blue',['Denmark','Estonia','Finland','Iceland','Latvia','Lithuania','Norway','Sweden']),
    'Southern Europe':
        ('yellow',[ 'Cyprus', 'Greece', 'Holy See', 'Italy', 'Malta', 'Portugal', 'San Marino', 'Spain', 'Turkey']),
    'Western Europe':
        ('green',['Andorra','Austria','Belgium','France','Germany','Ireland','Liechtenstein','Luxembourg','Monaco','Netherlands','Switzerland','United Kingdom'])
    }

for r,(color,cs) in regions.items():
    for c in cs:
        nodes['Region'][c] = r
        nodes['Color'][c] = color

nodes.sort_values(by='Region',inplace=True)
nodes.reset_index(inplace=True)

print(nodes)

# desenha o gráfico

hv.extension('bokeh')
hv.output(size=200)

edges = edges.merge(nodes,left_on='source',right_on='Country')
del edges['Country']
del edges['Region']
print(edges.head(3))

nodes = hv.Dataset(pd.DataFrame(nodes),'Country')

chord = hv.Chord((edges, nodes)) #.select(value=(5, None))
chord.opts(opts.Chord(edge_color='Color',labels='Country', node_color='Color'))

hv.save(chord,'eurovision.html')