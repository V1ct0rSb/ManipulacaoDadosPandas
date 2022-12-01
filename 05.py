# Podemos criar um DataFrame a partir de um dicionário, onde cada chave possui uma lista de elementos de igual tamanho.
# As chaves representam as colunas e cada um dos valores de sua lista representa o valor da linha correspondente para aquela coluna.
import pandas as pd 

personagens_df = pd.DataFrame({
    'nome': ['Luke Skywalker', 'Yoda', 'Palpatine'],
    'idade': [16, 1000, 70],
    'peso': [70.5, 15.2, 60.1],
    'eh jedi': [True, True, False]  # o nome das colunas podem ter espaços
})
print(personagens_df)
