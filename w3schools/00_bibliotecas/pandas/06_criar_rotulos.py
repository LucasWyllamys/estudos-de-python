# Se nada mais for especificado, os valores são rotulados com seu número de índice. O primeiro valor tem índice 0, o segundo valor tem índice 1, etc.
# Este rótulo pode ser usado para acessar um valor especificado:
import pandas as pd

lista = ["Lucas", "David", "Silas"]
serie = pd.Series(lista)
print(serie[0])    # Saída: Lucas (retorna o primeiro valor da série.)
print(serie)
''' Saída:
0    Lucas
1    David
2    Silas
dtype: object
'''

# Com o argumento index, você pode nomear seus próprios rótulos:
serie = pd.Series(lista, index=["filho_1", "filho_2", "filho_3"])
print(serie["filho_1"])     # Saída: Lucas
print(serie)
''' Saída:
filho_1    Lucas
filho_2    David
filho_3    Silas
dtype: object
'''