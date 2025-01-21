# A biblioteca pandas aqui foi instalada no ambiente virtual .venv.
# Quando você executa este arquivo, main.py, ele é executado entro do ambiente virtual .venv, ou seja, o compilador Python usado é o que está no .venv, bem como as bibliotecas que você baixa também são instaladas no ambiente virtual .venv.
import pandas as pd

df = pd.read_csv(r"arquivo_teste.csv")
print(df)
''' Saída:
     Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
..        ...    ...       ...       ...
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4

[169 rows x 4 columns]
'''