# Use o método close() para fechar o arquivo quando terminar de usá-lo:
file = open(r"w3schools\16_manipulacao_de_arquivos\1test.txt")
print(file.read())
file.close()
# Nota: Você deve sempre fechar seus arquivos. Em alguns casos, devido ao buffering, as alterações feitas em um arquivo podem não aparecer até que você feche o arquivo.
