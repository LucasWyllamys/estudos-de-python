# Você pode enviar qualquer tipo de dado de argumento para uma função (string, número, lista, dicionário etc.), e ele será tratado como o mesmo tipo de dado dentro da função.
# Por exemplo, se você enviar uma Lista como argumento, ela ainda será uma Lista quando chegar à função:
def my_function(food):
    print(food)     # Saída: ['apple', 'banana', 'cherry']

fruits = ["apple", "banana", "cherry"]

my_function(fruits) 