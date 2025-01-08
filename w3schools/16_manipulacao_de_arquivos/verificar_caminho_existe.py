# Importe o módulo 'os' e verifique se um caminho existe usando o método os.path.exists():
import os

# Verifica se um arquivo existe:
print(os.path.exists(r"w3schools\16_manipulacao_de_arquivos\1test.txt"))    # Saída: True ou False

# Verifica se a pasta existe:
print(os.path.exists(r"w3schools\16_manipulacao_de_arquivos"))    # Saída: True ou False