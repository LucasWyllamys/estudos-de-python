# A função principal para trabalhar com arquivos em Python é a função open().
# A função open() recebe dois parâmetros: nome do arquivo e modo:
''' Existem quatro métodos (modos) diferentes para abrir um arquivo:
Modo            Descrição
"r"             Ler - Valor padrão. Abre um arquivo para leitura, erro se o arquivo não existir.
"a"             Acrescentar - Abre um arquivo para anexar ao final do arquivo, cria o arquivo se ele não existir.
"w"             Escrever - Abre um arquivo para escrita, cria o arquivo se ele não existir.
"x"             Criar - Cria o arquivo especificado, retorna um erro se o arquivo existir.
'''
''' Além disso, você pode especificar se o arquivo deve ser tratado como modo binário ou texto:
Modo            Descrição
"t"             Texto - Valor padrão. Modo de texto.
"b"             Binário - Modo binário (por exemplo, imagens).
'''

# Para abrir um arquivo para leitura basta especificar o nome do arquivo:

file = open(r"w3schools\16_manipulacao_de_arquivos\1test.txt")
# O código acima é o mesmo que:
# Como "r" para leitura e "t" para texto são os valores padrão, você não precisa especificá-los:
file = open(r"w3schools\16_manipulacao_de_arquivos\1test.txt", "rt")
file.close()
