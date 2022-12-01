import pandas as pd

# Importando DataSets
# Para carregar um dataset no formato csv, basta utilizar a função read_csv do pandas.
data = pd.read_csv('./DataSets/GasPricesinBrazil_2004-2019.csv')
print(data)


# Carregando o dataset corretamente ==> neste caso, usa o separador ';'
data = pd.read_csv('./DataSets/GasPricesinBrazil_2004-2019.csv', sep=';')
print(data)
