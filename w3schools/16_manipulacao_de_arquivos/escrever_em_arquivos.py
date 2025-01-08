from datetime import datetime

# Escrever em um arquivo existente:
# Para gravar em um arquivo existente, você deve adicionar um parâmetro à função open():
    # "a"- Acrescentar - será anexado ao final do arquivo.
    # "w"- Escrever - substituirá qualquer conteúdo existente.

# Use o modo 'a' para abrir o arquivo e anexar o conteúdo ao arquivo:
file = open(r"w3schools\16_manipulacao_de_arquivos\1test.txt", "a")
file.write(f"\nAgora o arquivo tem mais conteúdo! {datetime.now()}")
file.close()
# Abre e ler o arquivo após o acréscimo:
file = open(r"w3schools\16_manipulacao_de_arquivos\1test.txt", "r")
print(file.read())
file.close()

# Use o modo 'w' para abrir o arquivo e sobrescrever o conteúdo do arquivo:
file = open(r"w3schools\16_manipulacao_de_arquivos\2test.txt", "w")
file.write(f"Conteúdo que sobrescreveu o conteúdo do arquivo! {datetime.now()}")
file.close()
# Observação: o método "w" substituirá o arquivo inteiro.
# Abre e ler o arquivo após o acréscimo:
file = open(r"w3schools\16_manipulacao_de_arquivos\2test.txt", "r")
print(file.read())
file.close()
