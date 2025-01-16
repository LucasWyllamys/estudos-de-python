# Os conjuntos de dados no Pandas geralmente são tabelas multidimensionais, chamadas DataFrames.
# Uma série é como uma coluna, um DataFrame é a tabela inteira.

import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)     # Carrega dados em um objeto DataFrame.
print(df)
''' Saída:
   calories  duration
0       420        50
1       380        40
2       390        45
'''