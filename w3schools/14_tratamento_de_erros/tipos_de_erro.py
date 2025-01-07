# 1. Erros de Sintaxe: Ocorrem quando o código não segue a sintaxe correta do Python:
while True print('Olá mundo')   # Isso gera um SyntaxError porque falta um dois-pontos (:) após o while.
''' Saída:
  File "c:\Users\U350504\Documents\GitHub\estudos-de-python\w3schools\14_tratamento_de_erros\tipos_de_erro.py", line 2
    while True print('Olá mundo')   # Isso gera um SyntaxError porque falta um dois-pontos (:) após o while.
               ^^^^^
SyntaxError: invalid syntax
'''

''' 2. Exceções: Ocorrem durante a execução do programa, mesmo que a sintaxe esteja correta.
Error                           Description
ZeroDivisionError               Tentativa de dividir um número por zero.
NameError                       Uso de uma variável que não foi definida.
TypeError                       Operação realizada em tipos de dados incompatíveis.
ValueError                      Função recebe um argumento com o tipo correto, mas valor inapropriado.
IndexError                      Tentativa de acessar um índice que não existe em uma lista ou tupla.
KeyError                        Tentativa de acessar uma chave que não existe em um dicionário.
FileNotFoundError               Tentativa de abrir um arquivo que não existe.
AttributeError                  Tentativa de acessar um atributo que não existe em um objeto.
'''
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")    # Saída: Erro: Divisão por zero não é permitida.