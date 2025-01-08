# Ler conteúdo do arquivo: A função open() retorna um objeto de arquivo, que possui um método read() para ler o conteúdo do arquivo:
file = open(r"w3schools\16_manipulacao_de_arquivos\test.txt", "r")
print(file.read())      
''' Saída: 
OlÃ¡! Bem-vindo ao test.txt         
Este arquivo Ã© para fins de teste. 
Boa sorte!
'''

# Ler somente partes do arquivo: Por padrão, o método read() retorna o texto inteiro, mas você também pode especificar quantos caracteres deseja retornar:
# Retorna os 5 primeiros caracteres do arquivo:
file = open(r"w3schools\16_manipulacao_de_arquivos\1test.txt", "r")
print(file.read(5))     # Saída: OlÃ¡!
file.close()

# Ler linhas: Você pode retornar uma linha usando o método readline():----------------------------------------------
file = open(r"w3schools\16_manipulacao_de_arquivos\1test.txt", "r")
print(file.readline())  # Saída: OlÃ¡! Bem-vindo ao test.txt
file.close()

# Chamando o método readline() duas vezes, você pode ler as duas primeiras linhas:
file = open(r"w3schools\16_manipulacao_de_arquivos\1test.txt", "r")
print(file.readline())  # Saída: OlÃ¡! Bem-vindo ao test.txt 
print(file.readline())  # Saída: Este arquivo Ã© para fins de teste.
file.close()
#-------------------------------------------------------------------------------------------------------------------

# Ao percorrer as linhas do arquivo, você pode ler o arquivo inteiro, linha por linha:
file = open(r"w3schools\16_manipulacao_de_arquivos\1test.txt", "r")
for linha in file:
    print(linha)  
file.close()
''' Saída:
OlÃ¡! Bem-vindo ao test.txt         

Este arquivo Ã© para fins de teste. 

Boa sorte!
'''
