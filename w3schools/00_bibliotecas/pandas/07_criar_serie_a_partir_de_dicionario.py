# Você também pode usar um objeto chave/valor, como um dicionário, ao criar uma Série:
# Nota: As chaves do dicionário se tornam os rótulos:
import pandas as pd

list_calories = {"day1": 420, "day2": 380, "day3": 390}

serie = pd.Series(list_calories)
print(serie)
''' Saída:
day1    420
day2    380
day3    390
dtype: int64
'''

# Para selecionar apenas alguns itens no dicionário, use o argumento index e especifique apenas os itens que deseja incluir na Série:
serie = pd.Series(list_calories, index=["day1", "day2"])
print(serie)
''' Saída:
day1    420
day2    380
dtype: int64
'''