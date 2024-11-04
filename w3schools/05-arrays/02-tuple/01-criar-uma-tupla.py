# Uma tupla é uma coleção ordenada e imutável.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)  # Saída: ('apple', 'banana', 'cherry')

# Para criar uma tupla com apenas um item, você precisa adicionar uma vírgula após o item, caso contrário, o Python não o reconhecerá como uma tupla:
thistuple = ("apple",)
print(type(thistuple))  # Saída: <class 'tuple'>
# NÃO é uma tupla!:
thistuple = ("apple")
print(type(thistuple))  # Saída: <class 'str'>
