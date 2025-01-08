# Para excluir um arquivo, você deve importar o módulo do sistema operacional e executar o método remove():
import os

if os.path.exists(r"w3schools\16_manipulacao_de_arquivos\4test.txt"):   # Verifica se o arquivo existe (gera erro se tentar excluir um arquivo que não existe).
    os.remove(r"w3schools\16_manipulacao_de_arquivos\4test.txt")    # Exclui o arquivo.
else:
    print("O arquivo não existe!")