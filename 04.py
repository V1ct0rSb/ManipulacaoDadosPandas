# Todo dataset carregado (dados estruturados) é um Data Frame: 'Tabela' bi-dimensional, de tamanho mutável, com dados potencialmente heterogêneos.

import pandas as pd

# Podemos acessar as dimensões do Data Frame (número de linhas x número de colunas) utilizando o atributo .shape do Data Frame.
data = pd.read_csv('./DataSets/GasPricesinBrazil_2004-2019.csv', sep=';')
print(data.shape)


print(
    f'O DataFrame possui {data.shape[0]} linhas/observações/registros e {data.shape[1]} colunas/atributos/variáveis.')
# O DataFrame possui 106823 linhas/observações/registros e 21 colunas/atributos/variáveis.
