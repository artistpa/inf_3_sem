import pandas as pd

path_p = input()
path_l = input()

papers = pd.read_csv(path_p, sep=';')
links = pd.read_csv(path_l, sep=';')

citations = links.groupby('reference').size()
papers['citations'] = papers.title.map(citations).fillna(0)

authors = (
    papers
    .groupby('author')
    ['citations']
    .mean()
    .sort_values(ascending=False)
)

for author, c in authors.head(3).items():
    print(author, f'{c:.3f}', sep=' ')
