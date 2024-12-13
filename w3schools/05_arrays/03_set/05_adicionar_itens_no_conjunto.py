# Depois que um conjunto é criado, você não pode alterar seus itens, mas pode adicionar novos itens.
# Para adicionar um item a um conjunto, use o add() método:
thisSet = {"apple", "banana", "cherry"}

thisSet.add("orange")

print(thisSet)  # Saída: {'cherry', 'apple', 'orange', 'banana'}

# Para adicionar itens de outro conjunto ao conjunto atual, use o método update():
thisSet = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisSet.update(tropical)

print(thisSet)
# Saída: {'papaya', 'banana', 'apple', 'pineapple', 'cherry', 'mango'}

# O objeto no método update() não precisa ser um conjunto, pode ser qualquer objeto iterável (tuplas, listas, dicionários etc.).
thisSet = {"apple", "banana", "cherry"}
myList = ["kiwi", "orange"]

thisSet.update(myList)

print(thisSet)  # Saída: {'cherry', 'kiwi', 'banana', 'orange', 'apple'}
