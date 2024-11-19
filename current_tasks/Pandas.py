import pandas as pd

dfg = pd.read_csv(input(), delimiter=';', index_col='id')
dfr = pd.read_csv(input(), delimiter=';', index_col='id')
dfg.loc[:, 'mean_mark'] = dfr.groupby('id').mean().mark
for val in dfg.sort_values(by='mean_mark', ascending=False).loc[:,['name', 'mean_mark']].head(3).values:
    print(val[0], "%.3f" % val[1])
res = dfg[dfg['mean_mark'] > 8.0].loc[:,['company', 'mean_mark']].groupby('company').count().sort_values(by='mean_mark', ascending=False).head(1)
print(res.iloc[0].name, res.loc[:, 'mean_mark'].values[0])

