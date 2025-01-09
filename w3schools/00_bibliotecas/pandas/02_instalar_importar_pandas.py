# Se você já tiver o Python e o PIP instalados em um sistema, a instalação do Pandas será muito fácil.
# Instale-o usando este comando: C:\Users\Your Name> pip install pandas

# Importar Pandas: Depois que o Pandas estiver instalado, importe-o em seus aplicativos adicionando a palavra-chave import:
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