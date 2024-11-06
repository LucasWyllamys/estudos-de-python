# Dicionários são usados ​​para armazenar valores de dados em pares chave:valor.
# Um dicionário é uma coleção ordenada*, mutável e que não permite duplicatas.
# Os dicionários são escritos com chaves e têm chaves e valores:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)  # Saída: {'brad': 'Ford', 'model': 'Mustang', 'year': 1964}

# Os itens do dicionário são apresentados em pares chave:valor e podem ser referenciados usando o nome da chave:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict["brand"])    # Saída: Ford

# Os valores nos itens do dicionário podem ser de qualquer tipo de dados:
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(thisdict)
# Saída: {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

# Os dicionários não podem ter dois itens com a mesma chave.
# Valores duplicados substituirão os valores existentes:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}

print(thisdict)  # Saída: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Da perspectiva do Python, os dicionários são definidos como objetos com o tipo de dados 'dict':
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(type(thisdict))   # Saída: <class 'dict'>
