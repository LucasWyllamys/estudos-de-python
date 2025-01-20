# Uma maneira comum de substituir células vazias é calcular a média, a mediana ou o valor da moda da coluna.
# O Pandas usa os métodos mean() median()e mode() para calcular os respectivos valores para uma coluna especificada.

# Calcule a MÉDIA e substitua quaisquer valores vazios por ela:
# Média = valor médio (a soma de todos os valores dividida pelo número de valores).
import pandas as pd

df = pd.read_csv(r"w3schools\00_bibliotecas\pandas\arquivo_teste.csv")

media = df["Calories"].mean()    # O método mean() calcula a média da coluna Calories.
df.fillna({"Calories": media}, inplace=True)
print(df.head())
''' Saída:
   Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
3        45    109       175     282.4
4        45    117       148     406.0
'''

# Calcule a MEDIANA e substitua quaisquer valores vazios por ela:
# Mediana = o valor no meio, depois de você ter classificado todos os valores em ordem crescente.
mediana = df["Calories"].median()   # O método median() calcula a mediana da coluna Calories.
df.fillna({"Calories": mediana}, inplace=True)
print(df.head())
''' Saída:
   Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
3        45    109       175     282.4
4        45    117       148     406.0
'''

# Calcule a MODA e substitua quaisquer valores vazios por ele:
# Moda = o valor que aparece com mais frequência.
moda = df["Calories"].mode()[0]  # O método mode() calcula a moda da coluna Calories.
df.fillna({"Calories": moda}, inplace=True)
print(df.head())
''' Saída:
   Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
3        45    109       175     282.4
4        45    117       148     406.0
'''