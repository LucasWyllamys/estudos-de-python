# O método values() retornará uma lista de todos os valores no dicionário:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisDict.values()
print(x)    # Saída: dict_values(['Ford', 'Mustang', 1964])

# A lista de valores é uma visão do dicionário, o que significa que quaisquer alterações feitas no dicionário serão refletidas na lista de valores:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
print(x)    # Saída: dict_values(['Ford', 'Mustang', 1964])

car["year"] = 2020      # Modificação de item existente
car["color"] = "red"    # Novo item

print(x)    # Saída: dict_values(['Ford', 'Mustang', 2020, 'red'])
