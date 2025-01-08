''' Para criar um novo arquivo em Python, use o método open(), com um dos seguintes parâmetros:
"x" - Criar - criará um arquivo, retornará um erro se o arquivo existir.
"a" - Acrescentar - criará um arquivo se o arquivo especificado não existir.
"w" - Escrever - criará um arquivo se o arquivo especificado não existir.
'''

# Crie um arquivo chamado "myfile.txt":
file = open(r"w3schools\16_manipulacao_de_arquivos\3test.txt", "x")
file.close()
# Obs.: RETORNA UM ERRO SE O ARQUIVO JÁ EXISTIR!

# Crie um novo arquivo se ele não existir:
file = open(r"w3schools\16_manipulacao_de_arquivos\4test.txt", "w")
file.close()