import pandas as pd

personagens_df = pd.DataFrame({
    'nome': ['Luke Skywalker', 'Yoda', 'Palpatine'],
    'idade': [16, 1000, 70],
    'peso': [70.5, 15.2, 60.1],
    'eh jedi': [True, True, False]  # o nome das colunas podem ter espaços
})
# O atributo DataFrame.columns retorna uma "lista" com os nomes de todas as colunas do data frame.
print(personagens_df.columns)

# 01
# Para renomear colunas do data frame, utilize o método DataFrame.rename, que retorna uma cópia do data frame com as as colunas renomeadas:
personagens_df_renomeado = personagens_df.rename(columns={
    'nome': 'Nome Completo',  # renomeia a coluna de nome 'nome' para 'Nome Completo'
    'idade': 'Idade'
})
print(personagens_df_renomeado)

# Obs: Ele sempre vai retornar uma copia da original, então se der um print na tabela inicial ela vai está normal


# 02
# Para substituir a tabela inicial, utilize o parâmetro inplace=True
personagens_df.rename(columns={
    'nome': 'Nome Completo',
    'idade': 'Idade'
}, inplace=True)
print(personagens_df)


# 03
# Uma outra forma de renomear todas as colunas de um data frame é passar uma lista com os novos nomes das colunas para o atributo DataFrame.columns:
personagens_df.columns = ['NOME', 'IDADE', 'PESO', 'EH_JEDI']
print(personagens_df)
