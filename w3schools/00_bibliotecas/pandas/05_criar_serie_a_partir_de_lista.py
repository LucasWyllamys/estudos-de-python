# Uma série de Pandas é como uma coluna em uma tabela.
# É uma matriz unidimensional que contém dados de qualquer tipo.

# Cria uma série simples de Pandas a partir de uma lista:
import pandas as pd

lista = [1, 7, 2]
serie = pd.Series(lista)
print(serie)
''' Saída:
0    1
1    7
2    2
dtype: int64
'''