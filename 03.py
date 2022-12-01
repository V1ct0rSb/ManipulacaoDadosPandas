import pandas as pd

# .info() ==> vai retornar as informações do Dataset 
data = pd.read_csv('./DataSets/GasPricesinBrazil_2004-2019.csv', sep=';')
print(data.info())

# Obs: Esse object nas informações, no geral, representa strings