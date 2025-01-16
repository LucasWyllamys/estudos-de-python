import pandas as pd

data = {
    "calorias": [420, 380, 390],
    "duração": [50, 40, 45]
}

df = pd.DataFrame(data, index=["dia1", "dia2", "dia3"])
print(df)
''' Saída:
      calorias  duração
dia1       420       50
dia1       380       40
dia3       390       45
'''

# Use o índice nomeado no atributo loc para retornar a(s) linha(s) especificada(s):
print(df.loc["dia2"])
''' Saída:
calorias    380
duração      40
Name: dia2, dtype: int64
'''