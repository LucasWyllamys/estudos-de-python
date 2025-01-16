import pandas as pd

df = pd.read_csv(r"w3schools\00_bibliotecas\pandas\arquivo_teste.csv", delimiter=",")
print(df)
''' Saída:
     Duration  Pulse  Maxpulse Calories
0          60    110       130    409,1
1          60    117       145      479
2          60    103       135      340
3          45    109       175    282,4
4          45    117       148      406
..        ...    ...       ...      ...
164        60    105       140    290,8
165        60    110       145    300,4
166        60    115       145    310,2
167        75    120       150    320,4
168        75    125       150    330,4

[169 rows x 4 columns]
'''

# Use o método head() para retornar o cabeçalho as linhas especificadas:
# Se você não especificar a quantidade de linhas ele retornará as 5 primeiras:
print(df.head(10))  # Retorna o cabeçalho e as 10 primeiras linhas.
''' Saída:
   Duration  Pulse  Maxpulse Calories
0        60    110       130    409,1
1        60    117       145      479
2        60    103       135      340
3        45    109       175    282,4
4        45    117       148      406
5        60    102       127    300,5
6        60    110       136      374
7        45    104       134    253,3
8        30    109       133    195,1
9        60     98       124      269
'''