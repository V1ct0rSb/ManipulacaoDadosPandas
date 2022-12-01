import pandas as pd

# A função .head() exibe as 5 primeiras linhas do dataset/tabela/Data Frame.
# Lembrando que vai começar do 0 e vai até o 4
data = pd.read_csv('./DataSets/GasPricesinBrazil_2004-2019.csv', sep=';')
print(data.head())


# Exibe as 10 primeiras linhas do dataframe
data = pd.read_csv('./DataSets/GasPricesinBrazil_2004-2019.csv', sep=';')
print(data.head(10))
