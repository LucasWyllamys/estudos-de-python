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

# Os pandas usam o atributo loc para retornar os dados de uma ou mais linhas especificadas:
print(df.loc[0])    # Retorna uma série com os dados da linha 0.
''' Saída:
calories    420      
duration     50      
Name: 0, dtype: int64
'''

# Para retornar mais de uma linha, use uma lista de índices:
print(df.loc[[0, 1]])   # Retorna um DataFrame com os dados das linhas 0 e 1.
''' Saída:
   calories  duration
0       420        50
1       380        40
'''