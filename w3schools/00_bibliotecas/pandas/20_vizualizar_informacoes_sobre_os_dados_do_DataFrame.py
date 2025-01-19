# O objeto DataFrame tem um método chamado info(), que fornece mais informações sobre o conjunto de dados:
import pandas as pd

df = pd.read_csv(r"w3schools\00_bibliotecas\pandas\arquivo_teste.csv")
print(df.info())
''' Saída:
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 169 entries, 0 to 168
    Data columns (total 4 columns):
    #   Column    Non-Null Count  Dtype  
    ---  ------    --------------  -----  
    0   Duration  169 non-null    int64  
    1   Pulse     169 non-null    int64  
    2   Maxpulse  169 non-null    int64  
    3   Calories  164 non-null    float64
    dtypes: float64(1), int64(3)
    memory usage: 5.4 KB
    None
'''
''' Resultado Explicado:
1. O resultado nos diz que há 169 linhas e 4 colunas:
  RangeIndex: 169 entradas, 0 a 168
  Colunas de dados (total de 4 colunas):

2. E o nome de cada coluna, com o tipo de dado:
   # Coluna Contagem não nula Dtype  
  --- ------ -------------- -----  
   0 Duração 169 não nulo int64  
   1 Pulso 169 não nulo int64  
   2 Maxpulse 169 não nulo int64  
   3 calorias 164 não nulo float64

3. Valores Nulos:
    O método info() também nos diz quantos valores não nulos estão presentes em cada coluna e, em nosso conjunto de dados, parece que há 164 de 169 valores não nulos na coluna "Calorias".
    O que significa que há 5 linhas sem valor algum na coluna "Calorias", por algum motivo.
'''