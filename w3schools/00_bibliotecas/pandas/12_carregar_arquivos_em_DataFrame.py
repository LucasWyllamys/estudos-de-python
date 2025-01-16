# Se seus conjuntos de dados estiverem armazenados em um arquivo, o Pandas poderá carregá-los em um DataFrame:
import pandas as pd

df = pd.read_csv(r"w3schools\00_bibliotecas\pandas\arquivo_teste.csv", delimiter=",")
print(df)   # Retorna a visualização das 5 primeiras e 5 últimas linhas do DataFrame.
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