# Iterável: É um objeto que pode ser iterado. Ele possui o método __iter__() que retorna um iterador. Listas, tuplas, dicionários e conjuntos são todos objetos iteráveis.
# Iterador: É um objeto que realiza a iteração, implementa os métodos especiais __iter__() e __next__(), permitindo que você percorra seus elementos um por um.
# __iter__(): Este método deve retornar o próprio objeto iterador. Ele é chamado quando um iterador é inicializado, por exemplo, ao usar um for loop.
# __next__(): Este método retorna o próximo item da sequência. Quando não há mais itens para retornar, ele deve levantar a exceção StopIteration.
myList = ["apple", "banana", "cherry"]    # Objeto Iterável
iterador = iter(myList)                   # Objeto Iterador (o método iter() retorna o objeo iterador a partir do objeto iterável).

# Use o método next() para obter os elementos do iterador um por um:
print(next(iterador))     # Saída: apple
print(next(iterador))     # Saída: banana
print(next(iterador))     # Saída: cherry
# print(next(iterador))   # Ativa StopIteration

print(iterador) # Saída: <list_iterator object at 0x00000271C6897760>

# O for loop, na verdade, cria um objeto iterador (__iter__()) e executa o método next() (__next__()) para cada loop:
myList = ["apple", "banana", "cherry"]

for x in myList:   
    print(x)
''' Saída:
apple
banana
cherry
'''