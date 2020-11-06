import pandas as pd

data_poverty = pd.read_excel('Data/revenu.xlsx', 'DEP')
data_poverty = data_poverty.iloc[5:, :]
data_poverty = data_poverty.iloc[:, [0, 1, 6]]
data_poverty.columns = ['Code', 'Département', 'Taux de pauvreté']
plus_pauvre = data_poverty.iloc[:, 2].min()
plus_riche = data_poverty.iloc[:, 2].max()
data_poverty.sort_values(by='Taux de pauvreté')
pauvrete = data_poverty.iloc[:, 2]
pauvrete.mean()
pauvrete.std()
pauvrete.median()

data_suicide = pd.read_csv('Data/taux-suicide.csv', sep=';')
data_suicide = data_suicide[2:]
data_suicide.columns = ['Code', 'Département', 'Taux de suicide']
data_suicide.sort_values(by='Taux de suicide', inplace=True)
data_suicide["Rank"] = data_suicide["Taux de suicide"].rank()
print(data_suicide)

