# Você não pode copiar uma lista simplesmente digitando list2 = list1, porque: list2será apenas uma referência a list1, e as alterações feitas em list1serão feitas automaticamente também em list2.
# Você pode usar o método copy() para copiar uma lista.
myList1 = ['maçã', 'uva', 'morango']
myList2 = myList1.copy()
print(myList2)  # Saída: ['maçã', 'uva', 'morango']

# Outra maneira de fazer uma cópia é usar o método list() interno.
# Faça uma cópia de uma lista com o método list():
myList1 = ['maçã', 'uva', 'morango']
myList2 = list(myList1)
print(myList2)  # Saída: ['maçã', 'uva', 'morango']

# Você também pode fazer uma cópia de uma lista usando o operador : (slice).
myList1 = ['maçã', 'uva', 'morango']
myList2 = myList1[:]
print(myList2)  # Saída: ['maçã', 'uva', 'morango']