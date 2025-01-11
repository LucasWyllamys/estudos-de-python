# Use o método DataFrame para construir um data frame do zero.
import pandas as pd

myDataSet = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}

df = pd.DataFrame(myDataSet)
print(df)
''' Saída:
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2
'''