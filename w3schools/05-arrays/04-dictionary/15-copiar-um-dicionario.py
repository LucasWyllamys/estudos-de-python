# Você não pode copiar um dicionário simplesmente digitando dict2 = dict1, porque: dict2 será apenas uma referência a dict1, e as alterações feitas em dict1 serão feitas automaticamente também em dict2.

# Há maneiras de fazer uma cópia, uma delas é usar o método copy():
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

myDict = thisDict.copy()
print(myDict)
# Saída: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Outra maneira de fazer uma cópia é usar a função interna dict():
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

myDict = dict(thisDict)
print(myDict)
# Saída: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
