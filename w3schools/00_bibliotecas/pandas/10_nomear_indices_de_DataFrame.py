import pandas as pd

data = {
    "calorias": [420, 380, 390],
    "duração": [50, 40, 45]
}

# Com o argumento index, você pode nomear seus próprios índices:
df = pd.DataFrame(data, index=["dia1", "dia2", "dia3"])
print(df)
''' Saída:
      calorias  duração
dia1       420       50
dia2       380       40
dia3       390       45
'''

