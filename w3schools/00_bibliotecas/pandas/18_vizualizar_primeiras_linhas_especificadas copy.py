# Um dos métodos mais utilizados para obter uma visão geral rápida do DataFrame é o método head().
# O método head() retorna os cabeçalhos e um número especificado de linhas, começando do topo.
# Observação: se o número de linhas não for especificado, o método head() retornará as 5 primeiras linhas.

# Obtém uma visão geral rápida imprimindo as primeiras 10 linhas do DataFrame:
import pandas as pd

df = pd.read_csv(r"w3schools\00_bibliotecas\pandas\arquivo_teste.csv")
print(df.head(10))   # Retorna o cabeçalho e as 10 primeiras linhas.
''' Saída:
      Duration  Pulse  Maxpulse  Calories
   0        60    110       130     409.1
   1        60    117       145     479.0
   2        60    103       135     340.0
   3        45    109       175     282.4
   4        45    117       148     406.0
   5        60    102       127     300.0
   6        60    110       136     374.0
   7        45    104       134     253.3
   8        30    109       133     195.1
   9        60     98       124     269.0
'''