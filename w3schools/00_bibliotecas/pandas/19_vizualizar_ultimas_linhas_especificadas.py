# O método tail() retorna os cabeçalhos e um número especificado de linhas, começando de baixo:
# Observação: se o número de linhas não for especificado, o método tail() retornará as 5 últimas linhas.
import pandas as pd

df = pd.read_csv(r"w3schools\00_bibliotecas\pandas\arquivo_teste.csv")
print(df.tail(10))   # Retorna o cabeçalho e as 10 últimas linhas.
''' Saída:
          Duration  Pulse  Maxpulse  Calories
     159        30     80       120     240.9
     160        30     85       120     250.4
     161        45     90       130     260.4
     162        45     95       130     270.0
     163        45    100       140     280.9
     164        60    105       140     290.8
     165        60    110       145     300.0
     166        60    115       145     310.2
     167        75    120       150     320.4
     168        75    125       150     330.4
'''