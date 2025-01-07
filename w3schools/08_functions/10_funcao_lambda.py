# Uma função lambda é uma pequena função anônima.
# Uma função lambda pode receber qualquer número de argumentos, mas só pode ter uma expressão.
'''
Sintaxe:
lambda arguments : expression
'''

# A expressão é executada e o resultado é retornado:
# Adicione 10 ao argumento a e retorne o resultado:
my_function = lambda a : a + 10
print(my_function(5))     # Saída: 15

# As funções lambda podem receber qualquer número de argumentos.
# Multiplique argumento a por argumento b e retorne o resultado:
my_function2 = lambda a, b : a * b
print(my_function2(5, 6))   # Saída: 30

my_function3 = lambda a, b, c : a + b + c
print(my_function3(5, 6, 2))    # Saída: 13

# O poder do lambda é melhor demonstrado quando você o usa como uma função anônima dentro de outra função.
# Digamos que você tenha uma definição de função que recebe um argumento, e esse argumento será multiplicado por um número desconhecido:
def myfunc(n):
    return lambda a : a * n

doubler = myfunc(2) # Use a definição de função para criar uma função que sempre dobra o número que você envia.
tripler = myfunc(3) # Ou use a mesma definição de função para criar uma função que sempre triplique o número que você enviar.

print(doubler(11))  # Saída: 22
print(tripler(11))  # Saída: 33

# NOTA: Use funções lambda quando uma função anônima for necessária por um curto período de tempo.

