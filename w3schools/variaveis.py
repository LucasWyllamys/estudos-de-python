# Variáveis não precisam ser declaradas com nenhum tipo específico

x = 5
y = 'Lucas'
print(x, y)  # Saída: 5 Lucas

# No Python, as variáveis podem até mesmo mudar de tipo depois de serem definidas

z = 4
z = 'teste'
print(z)  # Saída: teste

# Se você quiser especificar o tipo de dados de uma variável, isso pode ser feito com conversão

x = str(3)
y = int(3)
z = float(3)
print(x)  # Saída: '3'
print(y)  # Saída: 3
print(z)  # Saída: 3.0

# Como obter o tipo de uma variável

x = 5
y = 'Lucas'
print(type(x))  # Saída: <class 'int'>
print(type(y))  # Saída: <class 'str'>

# Variáveis de string podem ser declaradas usando aspas simples ou duplas

nome = "Lucas"
nome = 'Lucas'

# Como nomear variáveis multi palavras

meuNome = 'Lucas'  # Caso Camelo
MeuNome = 'Lucas'  # Caso Pascal
meu_nome = 'Lucas'  # Caso da Cobra

# Como atribuir valores para múltiplas várias variáveis em uma única linha

x, y, z = 'Laranja', 'Banana', 'Morango'
print(x)  # Saída: Laranja
print(y)  # Saída: Banana
print(z)  # Saída: Morango

# Como atribuir o mesmo valor a várias variáveis em uma única linha

x = y = z = "Laranja"
print(x)  # Saída: Laranja
print(y)  # Saída: Laranja
print(z)  # Saída: Laranja

# Como descompactar uma coleção

frutas = ['maçã', 'banana', 'morango']  # Exemplo com uma lista
x, y, z = frutas
print(x)  # Saída: maçã
print(y)  # Saída: banana
print(z)  # Saída: morango

# Como criar variáveis globais

x = 'teste'


def minhaFuncao1():
    print('Isso é um', x)


minhaFuncao1()  # Saída: Isso é um teste

"""
Se você criar uma variável com o mesmo nome dentro de uma função, essa variável será local, 
e só poderá ser usada dentro da função. A variável global com o mesmo nome permanecerá como era, 
global e com o valor original.
"""

a = 'teste1'


def minhaFuncao2():
    a = 'teste2'
    print('Isso é um', a)


minhaFuncao2()  # Saída: Isso é um teste2

# Como criar uma variável global dentro de uma função

def minhaFuncao3():
    global b
    b = 'teste3'


minhaFuncao3()

print('Isso é um', b)   # Saída: Isso é um teste3

# Como alterar o valor de uma variável global dentro de uma função

x = 'teste4'


def minhaFuncao4():
    global x
    x = 'teste5'


minhaFuncao4()

print('Isso é um', x)   # Saída: Isso é um teste5
