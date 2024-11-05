# Observação: ambos os métodos union() e update() excluirão quaisquer itens duplicados.

# O método union() retorna um novo conjunto com todos os itens de ambos os conjuntos.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)  # Saída: {'b', 1, 'a', 2, 3, 'c'}

# Você pode usar o operador | em vez do método union() e obterá o mesmo resultado:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# Todos os métodos e operadores de junção podem ser usados ​​para unir vários conjuntos.
# Ao usar um método, basta adicionar mais conjuntos entre parênteses, separados por vírgulas:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

mySet = set1.union(set2, set3, set4)
print(mySet)
# Saída: {'b', 1, 2, 3, 'cherry', 'apple', 'John', 'c', 'Elena', 'bananas', 'a'}

# Ao usar o operador |, separe os conjuntos com mais operadores |:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

mySet = set1 | set2 | set3 | set4
print(mySet)
# Saída: {1, 2, 3, 'John', 'bananas', 'c', 'cherry', 'apple', 'b', 'a', 'Elena'}

# O método union() permite que você junte um conjunto com outros tipos de dados, como listas ou tuplas.
# O resultado será um conjunto.
# Observação: o operador | só permite que você junte conjuntos com conjuntos, e não com outros tipos de dados, como você pode fazer com o método union().
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)  # Saída {1, 2, 'b', 3, 'a', 'c'}
