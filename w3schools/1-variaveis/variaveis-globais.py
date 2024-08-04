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