# Um for loop é usado para iterar sobre uma sequência (que pode ser uma lista, uma tupla, um dicionário, um conjunto ou uma string).
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
''' Saída:
apple
banana
cherry
'''

# Looping através de uma string:
# Mesmo as strings sendo objetos iteráveis, elas contêm uma sequência de caracteres:
for x in "banana":
    print(x)
''' Saída:
b
a
n
a
n
a
'''

# Com a instrução break podemos parar o loop antes que ele tenha percorrido todos os itens:
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        break
    print(x)
''' Saída:
apple
'''

# Com a instrução continue podemos parar a iteração atual do loop e continuar com a próxima:
# Não imprima banana:
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        continue
    print(x)
''' Saída:
apple
cherry
'''

# A função range():
# Acesse o arquivo: C:\Users\U350504\Documents\GitHub\estudos-de-python\w3schools\00-funcoes\range().py

# A palavra-chave else em um for loop especifica um bloco de código a ser executado quando o loop for concluído:
# Nota: O bloco else NÃO será executado se o loop for interrompido por uma instrução break.
for x in range(6):
    print(x)
else:
    print("FIM!")
''' Saída:
0
1
2
3
4
5
FIM!
'''

# Um loop aninhado é um loop dentro de um loop.
# O "loop interno" será executado uma vez para cada iteração do "loop externo":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
''' Saída:
red apple 
red banana
red cherry
big apple 
big banana
big cherry
tasty apple
tasty banana
tasty cherry
'''

# Os for loops não podem estar vazios, mas se por algum motivo você tiver um for loop sem conteúdo, insira-o na instrução pass para evitar obter um erro.
for x in [0, 1, 2]:
    pass
