# O Python tem um conjunto de funções matemáticas integradas, incluindo um extenso módulo matemático, que permite executar tarefas matemáticas em números.

# As funções min() e max() podem ser usadas para encontrar o menor ou maior valor em um iterável:
x = min(5, 10, 25)
y = max([5, 10, 25])
print(x)    # Saída: 5
print(y)    # Saída: 25

# A função abs() retorna o valor absoluto (positivo) do número especificado:
x = abs(-7.25)
print(x)    # Saída: 7.25

# A função pow(x, y) retorna o valor de x elevado à potência de y (x^y):
x = pow(4, 3)
print(x)    # Saída: 64

# A função sum() calcula a soma de todos os elementos de um iterável, como uma lista, tupla ou conjunto, ou ainda de qualquer outro objeto iterável que contenha números. Sintaxe: sum(iterable, start=0)
order = [
    {"price": 10.0, "quantity": 2},
    {"price": 5.0, "quantity": 4}
]
print(sum(item['price'] * item['quantity'] for item in order))  # Saída: 40.0