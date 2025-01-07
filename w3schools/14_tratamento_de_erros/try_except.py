''' Tratamento de exceções: Quando ocorre um erro, ou uma exceção, como chamamos, o Python normalmente para e gera uma mensagem de erro. Essas exceções podem ser tratadas usando a instrução try:

- try:
    Bloquo que permite que você teste um bloco de código em busca de erros.

- except:
    Bloco que permite que você lide com o erro.

- else:
    Bloco que permite que você execute código quando não há erro.

- finally:
    Bloco que permite que você execute código, independentemente do resultado dos blocos try e except.
'''

# try: Este bloco irá gerar uma exceção, pois x não está definido:
try:
    print(x)
except:
    print("Ocorreu uma exceção!")   # Saída: Ocorreu uma exceção!
# Como o bloco try gera um erro, o bloco except será executado.
# Sem o bloco try, o programa travaria e geraria um erro.

# except: Você pode definir quantos blocos de exceção quiser, por exemplo, se quiser executar um bloco especial de código para um tipo especial de erro:
# Imprima uma mensagem se o bloco try gerar um NameErrore, outra para outros erros:
try:
    print(x)
except NameError:
    print("A variável x não está definida!")    # Saída: A variável x não está definida!
except:
    print("Outra coisa deu errado.")

# else: Você pode usar a palavra-chave else para definir um bloco de código a ser executado se nenhum erro for gerado:
try:
    print("Hello")
except:
    print("Algo deu errado!")
else:
    print("Nada deu errado.")   # Saída: Nada deu errado.

# finally: Este bloco, se especificado, será executado independentemente se o bloco try gerar um erro ou não:
try:
    print(x)
except:
    print("Algo deu errado!")               # Saída: Algo deu errado!
finally:
    print("O 'try except' está concluído")  # Saída: O 'try except' está concluído
# Isso pode ser útil para fechar objetos e limpar recursos:
# Tente abrir e gravar em um arquivo que não é gravável:
try:
    file = open(r"w3schools\13_try_except\testfile.txt")
    try: 
        file.write("Testando o try.")
    except:
        print("Algo deu errado ao gravar no arquivo!")  # Saída: Algo deu errado ao gravar no arquivo!
    finally:
        file.close()
        print("Fecha arquivo.") # Saída: Fecha arquivo.
except:
    print("Algo deu errado ao abrir o arquivo!")
# O programa pode continuar, sem deixar o objeto de arquivo aberto.